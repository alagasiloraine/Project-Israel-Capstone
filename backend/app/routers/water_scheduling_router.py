from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from firebase_admin import firestore
from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime, timedelta
import requests
import time

router = APIRouter()

class Interval(BaseModel):
    value: int
    unit: str  # "days", "weeks", "hours"

class Schedule(BaseModel):
    dateTime: str
    duration: int
    mode: str
    days: List[bool]
    skipIfRain: bool
    notifyWatering: bool
    waterFlowRate: Union[float, str]
    interval: Optional[Interval] = None
    scheduledTime: Optional[int] = None
    completed: bool = Field(default=False)

class WateringLog(BaseModel):
    schedule_id: str
    executed_at: int
    duration: int
    device_id: str
    status: str

def compute_next_epoch(schedule: Schedule) -> int:
    now = datetime.now()
    try:
        selected = datetime.strptime(schedule.dateTime, "%a, %b %d, %I:%M %p")
    except ValueError:
        try:
            selected = datetime.strptime(schedule.dateTime, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            print("❌ Failed to parse dateTime")
            return 0

    target_time = selected.time()
    day_of_month = selected.day

    if schedule.mode == "calendar-day":
        year, month = now.year, now.month
        for _ in range(24):
            try:
                candidate = datetime(year, month, day_of_month, target_time.hour, target_time.minute)
                if candidate > now:
                    return int(candidate.timestamp())
            except ValueError:
                pass
            month += 1
            if month > 12:
                month = 1
                year += 1
        return 0

    if schedule.mode == "one-time":
        return schedule.scheduledTime or int(selected.timestamp())

    if schedule.mode == "daily":
        dt = datetime.combine(now.date(), target_time)
        if dt <= now:
            dt += timedelta(days=1)
        return int(dt.timestamp())

    if schedule.mode == "weekly":
        today = now.weekday()
        for i in range(0, 7):
            day_index = (today + i) % 7
            if schedule.days[day_index]:
                candidate_date = now.date() + timedelta(days=i)
                dt = datetime.combine(candidate_date, target_time)
                if dt > now:
                    return int(dt.timestamp())
        return int(now.timestamp() + 86400)

    if schedule.mode == "custom" and schedule.interval:
        dt = datetime.combine(now.date(), target_time)
        interval_days = schedule.interval.value if schedule.interval.unit == "days" else 0
        while dt <= now:
            dt += timedelta(days=interval_days)
        return int(dt.timestamp())

    return 0

@router.post("/api/watering-schedule")
def save_schedule(schedule: Schedule):
    try:
        print("📥 Step 1: Backend received watering schedule:")
        print(schedule)

        if schedule.mode != "one-time":
            schedule.scheduledTime = compute_next_epoch(schedule)
            print(f"⏱ Computed next epoch: {schedule.scheduledTime}")

        if schedule.scheduledTime and schedule.scheduledTime > 1_000_000_000_000:
            print("⚙️ Converting scheduledTime from ms to s...")
            schedule.scheduledTime = int(schedule.scheduledTime / 1000)

        print(f"💾 Final scheduledTime to send: {schedule.scheduledTime}")

        # Convert numpy.bool_ values to native Python bool
        schedule_data = schedule.dict()
        schedule_data["completed"] = False
        schedule_data["days"] = [bool(d) for d in schedule_data.get("days", [])]

        # Add createdAt timestamp
        schedule_data["createdAt"] = datetime.now().isoformat()

        print("✅ Final data being sent to ESP32:", schedule_data)

        current_epoch = int(time.time())
        schedule_payload = {**schedule_data, "currentTime": current_epoch}

        esp_ip = "192.168.1.21"
        esp_url = f"http://{esp_ip}/watering-schedule"
        print(f"🌐 Step 2: Sending watering schedule to ESP32 at {esp_url}...")

        try:
            response = requests.post(esp_url, json=schedule_payload, timeout=5)
            if response.status_code == 200:
                print("✅ Step 3: ESP32 acknowledged schedule.")
            else:
                print(f"⚠️ Step 3: ESP32 responded with status code: {response.status_code}")
        except Exception as esp_error:
            print(f"❌ Step 3: Failed to send schedule to ESP32: {esp_error}")

        return JSONResponse(content={"status": "success"})

    except Exception as e:
        print(f"❌ Error during schedule processing: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})


@router.get("/api/watering-schedule")
def get_next_schedule():
    try:
        db = firestore.client()
        schedules = db.collection("watering_schedules").order_by("scheduledTime", direction=firestore.Query.ASCENDING).stream()

        for doc in schedules:
            data = doc.to_dict()
            if data.get("completed") is True:
                continue

            schedule = Schedule(**data)
            next_epoch = compute_next_epoch(schedule)

            if next_epoch > int(time.time()):
                print(f"✅ Sending next schedule - Epoch: {next_epoch}")
                return JSONResponse(content={
                    "nextWateringEpoch": next_epoch * 1000,
                    "duration": schedule.duration
                })

        print("⚠️ No valid future schedule found.")
        return JSONResponse(content={"nextWateringEpoch": 0, "duration": 0})

    except Exception as e:
        print(f"❌ Failed to fetch next schedule: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post("/api/watering-schedule/complete")
def mark_schedule_complete():
    try:
        db = firestore.client()
        schedules = db.collection("watering_schedules").order_by("scheduledTime", direction=firestore.Query.ASCENDING).stream()

        for doc in schedules:
            data = doc.to_dict()
            doc_ref = db.collection("watering_schedules").document(doc.id)

            scheduled_time_ms = data.get("scheduledTime", 0)
            scheduled_time_sec = int(scheduled_time_ms / 1000) if scheduled_time_ms > 1000000000000 else scheduled_time_ms

            if not data.get("completed", False) and scheduled_time_sec <= int(time.time()):
                if data.get("mode") in ["one-time", "calendar-day"]:
                    doc_ref.update({"completed": True})
                    print(f"✅ Schedule marked completed: {doc.id}")
                    return JSONResponse(content={"status": "completed", "id": doc.id})
                else:
                    print(f"🔁 Recurring schedule NOT marked complete: {doc.id}")
                    return JSONResponse(content={"status": "recurring", "id": doc.id})

        print("⚠️ No running or past schedule to mark as completed.")
        return JSONResponse(content={"status": "no-action"})

    except Exception as e:
        print(f"❌ Failed to complete schedule: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post("/api/watering-log")
async def log_watering(req: Request):
    try:
        body = await req.json()
        log = WateringLog(**body)

        db = firestore.client()
        db.collection("watering_logs").add(log.dict())

        print(f"📝 Watering logged for schedule: {log.schedule_id}")
        return JSONResponse(content={"status": "logged"})

    except Exception as e:
        print(f"❌ Failed to log watering: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
