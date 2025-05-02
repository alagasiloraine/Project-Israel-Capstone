from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import httpx

router = APIRouter(
    prefix="/api/motor_status",
    tags=["Motor Status"]
)

# Set your ESP32 actual IP address here
ESP32_IP = "http://192.168.1.32"   # Replace this with your real ESP32 IP
ESP32_ENDPOINT = f"{ESP32_IP}/motor-status"

class MotorStatus(BaseModel):
    status: bool
    device_id: str
    user: str
    timestamp: datetime
    formatted_time: str

@router.post("/")
async def save_motor_status(status_data: MotorStatus):
    print("✅ Received toggle from Vue frontend")
    print(status_data.dict())

    # ✅ Now forward to ESP32
    try:
        payload = {"status": status_data.status}
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(ESP32_ENDPOINT, json=payload)
            response.raise_for_status()
        print("✅ Successfully forwarded to ESP32.")
    except Exception as e:
        print("❌ Failed to forward to ESP32:", e)
        raise HTTPException(status_code=500, detail="Could not forward to ESP32")

    return {"message": "Motor status received and forwarded"}
