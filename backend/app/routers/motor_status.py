from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix="/api/motor-status",
    tags=["Motor Status"]
)

class MotorStatus(BaseModel):
    status: bool
    device_id: str
    user: str
    timestamp: datetime
    formatted_time: str

@router.post("/")
async def save_motor_status(status_data: MotorStatus):
    # Example logic to save to DB or log
    print("Received motor status:", status_data)
    # You could save this to a database here
    return {"message": "Motor status received", "data": status_data}
