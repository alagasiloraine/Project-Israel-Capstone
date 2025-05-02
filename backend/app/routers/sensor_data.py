# from fastapi import APIRouter
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# from typing import List
# import asyncio
# import json
# from fastapi.encoders import jsonable_encoder
# import firebase_admin
# from firebase_admin import credentials, auth, firestore
# import os
# from dotenv import load_dotenv

# router = APIRouter()

# load_dotenv()

# # Load Firebase credentials dynamically
# FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
# if not FIREBASE_CREDENTIALS:
#     raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

# # Initialize Firebase App (Singleton)
# if not firebase_admin._apps:  # Prevent re-initialization
#     cred = credentials.Certificate(FIREBASE_CREDENTIALS)
#     firebase_admin.initialize_app(cred)

# # Firestore client
# db = firestore.client()

# # List of queues (each frontend connection gets its own)
# subscribers: List[asyncio.Queue] = []

# # Sensor data model (NPK, pH, temp, humidity)
# class SensorData(BaseModel):
#     nitrogen: float
#     phosphorus: float
#     potassium: float
#     soilpH: float
#     temperature: float
#     humidity: float

# # POST endpoint (optional external posting like Postman or test)
# @router.post("/sensor-data")
# async def receive_sensor_data(data: SensorData):
#     message = data.dict()

#     # Print to terminal
#     print("📡 Received Sensor Data via HTTP POST:")
#     for key, value in message.items():
#         print(f"  {key}: {value}")

#     # Send to all connected Vue frontends
#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "Data broadcasted"}

# # GET endpoint for frontend to receive real-time data
# @router.get("/stream")
# async def stream_sensor_data():
#     queue = asyncio.Queue()
#     subscribers.append(queue)

#     async def event_generator():
#         try:
#             while True:
#                 data = await queue.get()
#                 # ✅ Ensure valid JSON string for Vue frontend
#                 yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
#         except asyncio.CancelledError:
#             pass
#         finally:
#             subscribers.remove(queue)

#     return StreamingResponse(event_generator(), media_type="text/event-stream")

# # Internal function for FastAPI to use (from main.py)
# async def forward_sensor_data(data_dict):
#     # print("📡 Received Sensor Data from Arduino (internal):")
#     # for key, value in data_dict.items():
#     #     print(f"  {key}: {value}")

#     for queue in subscribers:
#         await queue.put(data_dict)



from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, List
import asyncio
import json
import os
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

import firebase_admin
from firebase_admin import credentials, firestore

router = APIRouter(prefix="/api")

# === Firebase Initialization ===
load_dotenv()
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
if not FIREBASE_CREDENTIALS:
    raise ValueError("Firebase credentials not found in .env")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()
subscribers: List[asyncio.Queue] = []

# === Models ===
class SensorData(BaseModel):
    nitrogen: Optional[float] = None
    phosphorus: Optional[float] = None
    potassium: Optional[float] = None
    soilPh: Optional[float] = None
    soilMoisture: Optional[float] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    device_id: Optional[str] = None

class WaterLevelData(BaseModel):
    waterLevel: float
    device_id: Optional[str] = "ESP32-WATER"

# === POST: /api/sensor-data ===
@router.post("/sensor-data")
async def receive_sensor_data(data: SensorData):
    message = data.dict(exclude_none=True)  # Only send fields that exist

    print("📡 Received Sensor Data:")
    for key, value in message.items():
        print(f"  {key}: {value}")

    # Save to Firebase
    try:
        db.collection("sensor_readings").add({
            **message,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Sensor data saved to Firebase")
    except Exception as e:
        print("❌ Firebase save error:", e)

    # Broadcast to connected Vue clients
    for queue in subscribers:
        await queue.put(message)

    return {"message": "Sensor data processed successfully"}

# === POST: /api/water-data ===
@router.post("/water-data")
async def receive_water_data(data: WaterLevelData):
    print(f"📥 Water Level from {data.device_id}: {data.waterLevel}%")

    message = {
        "type": "water",
        "data": {
            "waterLevel": data.waterLevel,
            "device_id": data.device_id
        }
    }

    try:
        db.collection("water_level_readings").add({
            **message["data"],
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Water level saved to Firebase")
    except Exception as e:
        print("❌ Failed to save water level:", e)

    for queue in subscribers:
        await queue.put(message)

    return {"message": "Water level received"}

# === Real-Time Stream: /api/stream ===
@router.get("/stream")
async def stream_sensor_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            docs = db.collection("sensor_readings") \
                .order_by("timestamp", direction=firestore.Query.DESCENDING) \
                .limit(1).stream()
            for doc in docs:
                latest = doc.to_dict()
                if latest:
                    yield f"data: {json.dumps(jsonable_encoder(latest))}\n\n"
        except Exception as e:
            print("❌ Error loading last sensor data:", e)

        try:
            while True:
                data = await queue.get()
                yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

# === Real-Time Water Stream: /api/water-stream ===
@router.get("/water-stream")
async def stream_water_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            docs = db.collection("water_level_readings") \
                .order_by("timestamp", direction=firestore.Query.DESCENDING) \
                .limit(1).stream()
            for doc in docs:
                latest = doc.to_dict()
                if latest:
                    yield f"data: {json.dumps(jsonable_encoder({'type': 'water', 'data': latest}))}\n\n"
        except Exception as e:
            print("❌ Error loading water data:", e)

        try:
            while True:
                data = await queue.get()
                if isinstance(data, dict) and data.get("type") == "water":
                    yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

# === Internal Function for Serial Reader Integration ===
async def forward_sensor_data(data_dict):
    try:
        db.collection("sensor_readings").add({
            **data_dict,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Internal sensor data saved to Firebase")
    except Exception as e:
        print("❌ Firebase save error:", e)

    for queue in subscribers:
        await queue.put(data_dict)
