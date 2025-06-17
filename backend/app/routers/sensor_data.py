# from fastapi import APIRouter, HTTPException
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel
# from typing import List
# import asyncio
# import json
# import os
# from dotenv import load_dotenv
# from fastapi.encoders import jsonable_encoder

# import firebase_admin
# from firebase_admin import credentials, firestore

# router = APIRouter(prefix="/api")

# load_dotenv()

# FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
# if not FIREBASE_CREDENTIALS:
#     raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

# if not firebase_admin._apps:
#     cred = credentials.Certificate(FIREBASE_CREDENTIALS)
#     firebase_admin.initialize_app(cred)

# db = firestore.client()

# subscribers: List[asyncio.Queue] = []

# class SensorData(BaseModel):
#     nitrogen: float 
#     phosphorus: float 
#     potassium: float 
#     soilPh: float 
#     soilMoisture: float  
#     temperature: float 
#     humidity: float 

# class WaterLevelData(BaseModel):
#     waterLevel: float


# @router.post("/sensor-data")
# async def receive_sensor_data(data: SensorData):
#     message = data.dict()

#     print("📡 Received Sensor Data:")
#     for key, value in message.items():
#         print(f"  {key}: {value}")

#     try:
#         db.collection("sensor_readings").add({
#             **message,
#             "timestamp": firestore.SERVER_TIMESTAMP
#         })
#         print("✅ Data saved to Firebase")
#     except Exception as e:
#         print("❌ Failed to save to Firebase:", e)

#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "Data broadcasted and saved to Firebase"}

# @router.get("/stream")
# async def stream_sensor_data():
#     queue = asyncio.Queue()
#     subscribers.append(queue)

#     async def event_generator():
#         try:
#             while True:
#                 data = await queue.get()
#                 yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
#         except asyncio.CancelledError:
#             pass
#         finally:
#             subscribers.remove(queue)

#     return StreamingResponse(event_generator(), media_type="text/event-stream")

# async def forward_sensor_data(data_dict):
#     try:
#         db.collection("sensor_readings").add({
#             **data_dict,
#             "timestamp": firestore.SERVER_TIMESTAMP
#         })
#         print("✅ Data saved to Firebase (internal)")
#     except Exception as e:
#         print("❌ Firebase save error:", e)

#     for queue in subscribers:
#         await queue.put(data_dict)


# @router.post("/water-data")
# async def get_water_data(data: WaterLevelData):
#     water_level = data.waterLevel

#     print(f"📥 Received water level: {water_level}%")

#     message = {
#         "type": "water",
#         "data": {
#             "waterLevel": water_level
#         }
#     }

#     try:
#         db.collection("water_level_readings").add({
#             "waterLevel": water_level,
#             "timestamp": firestore.SERVER_TIMESTAMP
#         })
#         print("✅ Water level saved to Firebase")
#     except Exception as e:
#         print("❌ Failed to save water level to Firebase:", e)

#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "Water level received successfully"}


# @router.get("/water-stream")
# async def stream_sensor_data():
#     queue = asyncio.Queue()
#     subscribers.append(queue)

#     async def event_generator():
#         try:
#             while True:
#                 data = await queue.get()
#                 yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
#         except asyncio.CancelledError:
#             pass
#         finally:
#             subscribers.remove(queue)

#     return StreamingResponse(event_generator(), media_type="text/event-stream")



# from fastapi import APIRouter
# from fastapi.responses import StreamingResponse
# from pydantic import BaseModel, Extra
# from typing import List
# import asyncio
# import json
# import os
# from dotenv import load_dotenv
# from fastapi.encoders import jsonable_encoder

# import firebase_admin
# from firebase_admin import credentials, firestore

# router = APIRouter(prefix="/api")

# # Load Firebase
# load_dotenv()
# FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
# if not FIREBASE_CREDENTIALS:
#     raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

# if not firebase_admin._apps:
#     cred = credentials.Certificate(FIREBASE_CREDENTIALS)
#     firebase_admin.initialize_app(cred)

# db = firestore.client()
# subscribers: List[asyncio.Queue] = []

# # ========= MODELS =========

# class NPKSoilPHData(BaseModel):
#     nitrogen: float
#     phosphorus: float
#     potassium: float
#     soilPh: float

# class MoistureClimateData(BaseModel):
#     soilMoisture: float
#     temperature: float
#     humidity: float
#     device_id: str  # ✅ added this to support ESP32 payload

#     class Config:
#         extra = Extra.ignore  # ✅ allows extra fields like status, battery, etc.

# class WaterLevelData(BaseModel):
#     waterLevel: float

# # ========= ESP32-1 =========
# @router.post("/esp32-1")
# async def receive_npk_soilph(data: NPKSoilPHData):
#     message = {
#         "type": "esp32-1",
#         "data": data.dict()
#     }

#     print("📡 Received ESP32-1 Data:", message["data"])

#     try:
#         db.collection("sensor_readings").add({
#             **data.dict(),
#             "timestamp": firestore.SERVER_TIMESTAMP,
#             "device": "esp32-1"
#         })
#         print("✅ ESP32-1 data saved to Firebase")
#     except Exception as e:
#         print("❌ Firebase save error (ESP32-1):", e)

#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "ESP32-1 data received and broadcasted"}

# # ========= ESP32-2 =========
# @router.post("/esp32-2")
# async def receive_moisture_temp_hum(data: MoistureClimateData):
#     message = {
#         "type": "esp32-2",
#         "data": data.dict()
#     }

#     print("📡 Received ESP32-2 Data:", message["data"])

#     try:
#         db.collection("sensor_readings").add({
#             **data.dict(),
#             "timestamp": firestore.SERVER_TIMESTAMP,
#             "device": "esp32-2"
#         })
#         print("✅ ESP32-2 data saved to Firebase")
#     except Exception as e:
#         print("❌ Firebase save error (ESP32-2):", e)

#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "ESP32-2 data received and broadcasted"}

# # ========= ESP32-3 =========
# @router.post("/esp32-3")
# async def receive_water_level(data: WaterLevelData):
#     water_level = data.waterLevel

#     message = {
#         "type": "esp32-3",
#         "data": {
#             "waterLevel": water_level
#         }
#     }

#     print("📡 Received ESP32-3 Water Level:", water_level)

#     try:
#         db.collection("water_level_readings").add({
#             "waterLevel": water_level,
#             "timestamp": firestore.SERVER_TIMESTAMP,
#             "device": "esp32-3"
#         })
#         print("✅ Water level saved to Firebase")
#     except Exception as e:
#         print("❌ Firebase save error (ESP32-3):", e)

#     for queue in subscribers:
#         await queue.put(message)

#     return {"message": "ESP32-3 data received and broadcasted"}

# # ========= STREAM =========
# @router.get("/stream")
# async def stream_sensor_data():
#     queue = asyncio.Queue()
#     subscribers.append(queue)

#     async def event_generator():
#         try:
#             while True:
#                 data = await queue.get()
#                 yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
#         except asyncio.CancelledError:
#             pass
#         finally:
#             subscribers.remove(queue)

#     return StreamingResponse(event_generator(), media_type="text/event-stream")

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Extra
from typing import List
import asyncio
import json
import os
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

import firebase_admin
from firebase_admin import credentials, firestore

router = APIRouter(prefix="/api")

# === Firebase Init ===
load_dotenv()

FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
if not FIREBASE_CREDENTIALS:
    raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()

subscribers: List[asyncio.Queue] = []

# === Data Models ===

# ESP32-1
class NPKSoilPHData(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    soilPh: float

# ✅ ESP32-2: added device_id support
class MoistureClimateData(BaseModel):
    soilMoisture: float
    temperature: float
    humidity: float
    device_id: str  # ✅ Added this line

    class Config:
        extra = Extra.ignore  # ✅ Allows extra fields without error

# ESP32-3
class WaterLevelData(BaseModel):
    waterLevel: float

# ========= ESP32-1 ROUTE ==========
@router.post("/esp32-1")
async def receive_npk_soilph(data: NPKSoilPHData):
    message = {
        "type": "esp32-1",
        "data": data.dict()
    }

    print("📡 Received ESP32-1 Data:", message["data"])

    try:
        db.collection("3sensor_readings").document("esp32-1").collection("readings").add({
            **data.dict(),
            "timestamp": firestore.SERVER_TIMESTAMP,
            "device": "esp32-1"
        })
        print("✅ ESP32-1 data saved to Firebase")
    except Exception as e:
        print("❌ Firebase save error (ESP32-1):", e)

    for queue in subscribers:
        await queue.put(message)

    return {"message": "ESP32-1 data received and broadcasted"}

# ========= ESP32-2 ROUTE ==========
@router.post("/esp32-2")
async def receive_moisture_temp_hum(data: MoistureClimateData):
    print("🟢 Step 1: ESP32-2 endpoint hit")

    # Log raw received data
    print("📥 Raw Data Received:", data)

    # Prepare the message for broadcasting
    message = {
        "type": "esp32-2",
        "data": data.dict()
    }

    print("🟢 Step 2: Message formatted for broadcast")
    print("📦 Message Content:", message)

    # Try to save to Firebase
    try:
        print("🟢 Step 3: Attempting to save to Firestore")
        db.collection("3sensor_readings").document("esp32-2").collection("readings").add({
            **data.dict(),
            "timestamp": firestore.SERVER_TIMESTAMP,
            "device": "esp32-2"
        })
        print("✅ Step 4: Data successfully saved to Firebase")
    except Exception as e:
        print("❌ Step 4: Firebase save error (ESP32-2):", e)

    # Broadcast the message to all subscribers
    print("🟢 Step 5: Broadcasting message to subscribers...")
    for queue in subscribers:
        await queue.put(message)
    print("📤 Step 6: Broadcast complete")

    return {"message": "ESP32-2 data received and broadcasted"}

# ========= ESP32-3 ROUTE ==========
@router.post("/esp32-3")
async def receive_water_level(data: WaterLevelData):
    water_level = data.waterLevel

    message = {
        "type": "esp32-3",
        "data": {
            "waterLevel": water_level
        }
    }

    print("📡 Received ESP32-3 Water Level:", water_level)

    try:
        db.collection("3sensor_readings").document("esp32-3").collection("readings").add({
            "waterLevel": water_level,
            "timestamp": firestore.SERVER_TIMESTAMP,
            "device": "esp32-3"
        })
        print("✅ ESP32-3 data saved to Firebase")
    except Exception as e:
        print("❌ Firebase save error (ESP32-3):", e)

    for queue in subscribers:
        await queue.put(message)

    return {"message": "ESP32-3 data received and broadcasted"}

# ========= UNIFIED STREAM ==========
@router.get("/stream")
async def stream_sensor_data():
    queue = asyncio.Queue()
    subscribers.append(queue)

    async def event_generator():
        try:
            while True:
                data = await queue.get()
                print(f"📤 Sending to frontend → variable: 'data' | value: {data}")
                yield f"data: {json.dumps(jsonable_encoder(data))}\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            subscribers.remove(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")