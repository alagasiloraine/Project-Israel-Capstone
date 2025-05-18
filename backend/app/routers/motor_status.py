from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix="/api",
    tags=["Motor Status"]
)

class MotorStatus(BaseModel):
    status: bool
    device_id: str
    user: str
    timestamp: datetime
    formatted_time: str

@router.post("/motor-status")
async def save_motor_status(status_data: MotorStatus):
    print("Received motor status:", status_data)
    return {"message": "Motor status received", "data": status_data}
