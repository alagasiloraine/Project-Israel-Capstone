from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
import asyncio
import json
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# List of queues (each frontend connection gets its own)
subscribers: List[asyncio.Queue] = []

# Sensor data model (NPK, pH, temp, humidity)
class SensorData(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    soilPh: float 
    soilMoisture: float  # Optional if you want to keep using it later
    temperature: float
    humidity: float

# POST endpoint (optional external posting like Postman or test)
@router.post("/sensor-data")
async def receive_sensor_data(data: SensorData):
    message = data.dict()

    # Print to terminal
    print("📡 Received Sensor Data via HTTP POST:")
    for key, value in message.items():
        print(f"  {key}: {value}")

    # Send to all connected Vue frontends
    for queue in subscribers:
        await queue.put(message)

    return {"message": "Data broadcasted"}

# GET endpoint for frontend to receive real-time data
@router.get("/stream")
async def stream_sensor_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            while True:
                data = await queue.get()
                # ✅ Ensure valid JSON string for Vue frontend
                yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

# Internal function for FastAPI to use (from main.py)
async def forward_sensor_data(data_dict):
    # print("📡 Received Sensor Data from Arduino (internal):")
    # for key, value in data_dict.items():
    #     print(f"  {key}: {value}")

    for queue in subscribers:
        await queue.put(data_dict)



