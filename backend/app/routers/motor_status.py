from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import httpx

# Router configuration
router = APIRouter(
    prefix="/api/motor_status",
    tags=["Motor Status"]
)

# ESP32 Configuration
ESP32_IP = "http://192.168.1.21"   # Change this if your ESP32 has a new IP
ESP32_ENDPOINT = f"{ESP32_IP}/motor-status"

# Data model
class MotorStatus(BaseModel):
    status: bool
    device_id: str
    user: str
    timestamp: datetime
    formatted_time: str

# Route to handle motor toggle
@router.post("/")
async def save_motor_status(status_data: MotorStatus):
    print("✅ Received toggle from Vue frontend")
    print(status_data.dict())

    payload = {
        "status": status_data.status
    }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(ESP32_ENDPOINT, json=payload)
            response.raise_for_status()

        try:
            response_data = response.json()
        except Exception:
            response_data = response.text  # fallback to raw text if ESP32 didn't return JSON

        print("✅ Successfully forwarded to ESP32.")
        return {
            "message": "Motor status received and forwarded",
            "esp32_response": response_data
        }

    except httpx.RequestError as e:
        print(f"❌ Network error: {e}")
        raise HTTPException(status_code=500, detail=f"Network error: {e}")

    except httpx.HTTPStatusError as e:
        print(f"❌ ESP32 responded with HTTP {e.response.status_code}")
        print("📩 ESP32 response body:", e.response.text)
        raise HTTPException(status_code=500, detail=f"ESP32 error: {e.response.text}")
