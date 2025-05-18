from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
import asyncio
import json
import os
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

import firebase_admin
from firebase_admin import credentials, firestore

router = APIRouter(prefix="/api")

load_dotenv()

FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
if not FIREBASE_CREDENTIALS:
    raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()

subscribers: List[asyncio.Queue] = []

class SensorData(BaseModel):
    nitrogen: float 
    phosphorus: float 
    potassium: float 
    soilPh: float 
    soilMoisture: float  
    temperature: float 
    humidity: float 

class WaterLevelData(BaseModel):
    waterLevel: float


@router.post("/sensor-data")
async def receive_sensor_data(data: SensorData):
    message = data.dict()

    print("📡 Received Sensor Data:")
    for key, value in message.items():
        print(f"  {key}: {value}")

    try:
        db.collection("sensor_readings").add({
            **message,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Data saved to Firebase")
    except Exception as e:
        print("❌ Failed to save to Firebase:", e)

    for queue in subscribers:
        await queue.put(message)

    return {"message": "Data broadcasted and saved to Firebase"}

@router.get("/stream")
async def stream_sensor_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            while True:
                data = await queue.get()
                yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

async def forward_sensor_data(data_dict):
    try:
        db.collection("sensor_readings").add({
            **data_dict,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Data saved to Firebase (internal)")
    except Exception as e:
        print("❌ Firebase save error:", e)

    for queue in subscribers:
        await queue.put(data_dict)


@router.post("/water-data")
async def get_water_data(data: WaterLevelData):
    water_level = data.waterLevel

    print(f"📥 Received water level: {water_level}%")

    message = {
        "type": "water",
        "data": {
            "waterLevel": water_level
        }
    }

    try:
        db.collection("water_level_readings").add({
            "waterLevel": water_level,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
        print("✅ Water level saved to Firebase")
    except Exception as e:
        print("❌ Failed to save water level to Firebase:", e)

    for queue in subscribers:
        await queue.put(message)

    return {"message": "Water level received successfully"}


@router.get("/water-stream")
async def stream_sensor_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            while True:
                data = await queue.get()
                yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")