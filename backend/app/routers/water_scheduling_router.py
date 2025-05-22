# from fastapi import APIRouter, Request
# from fastapi.responses import JSONResponse
# from firebase_admin import firestore
# from datetime import datetime
# import pytz

# router = APIRouter()

# @router.get("/api/watering-schedules")
# def get_filtered_schedules(request: Request):
#     try:
#         print(f"📡 API Hit: {request.client.host} | User-Agent: {request.headers.get('user-agent')}")
        
#         db = firestore.client()
#         ref = db.collection("watering_schedules")
#         docs = ref.stream()

#         schedules = []
#         now = datetime.now(pytz.timezone("Asia/Manila"))
#         print(f"📅 Current datetime (Asia/Manila): {now}")

#         for doc in docs:
#             data = doc.to_dict()
#             mode = data.get("mode", "weekly")
#             raw_datetime = data.get("dateTime", "")
#             duration = data.get("duration", 0)
#             days = data.get("days", [False]*7)

#             print(f"📄 Processing doc ID: {doc.id}")
#             print(f"🧩 Mode: {mode} | Raw datetime: {raw_datetime} | Duration: {duration} | Days: {days}")

#             formatted_datetime = ""
#             is_valid = False

#             try:
#                 if mode == "one-time":
#                     dt = datetime.strptime(raw_datetime, "%a, %b %d, %I:%M %p")
#                     dt = pytz.timezone("Asia/Manila").localize(dt)
#                     print(f"🕒 Parsed one-time datetime: {dt}")

#                     if dt >= now:
#                         formatted_datetime = dt.strftime("%Y-%m-%d %H:%M")
#                         is_valid = True
#                     else:
#                         print("⏭️ Skipped: one-time schedule is in the past.")
#                 else:
#                     parts = raw_datetime.split(",")
#                     if len(parts) >= 3:
#                         schedule_day = parts[0].strip()
#                         time_part = parts[2].strip().split(" ")[0]
#                         formatted_datetime = f"{schedule_day}, {time_part}"

#                         today_index = now.weekday()
#                         print(f"📆 Today is weekday index {today_index}")

#                         if mode == "daily":
#                             is_valid = True
#                         elif days[today_index]:
#                             is_valid = True
#                         else:
#                             print("⏭️ Skipped: schedule is not set for today.")
#             except Exception as e:
#                 print(f"⚠️ Failed to parse datetime for {doc.id}: {e}")
#                 continue

#             if is_valid:
#                 schedules.append({
#                     "id": doc.id,
#                     "dateTime": formatted_datetime,
#                     "days": days,
#                     "duration": duration,
#                     "mode": mode
#                 })

#         if schedules:
#             print(f"✅ {len(schedules)} valid schedule(s) ready to be sent.")
#         else:
#             print("📦 Returning 0 valid schedules.")

#         return JSONResponse(content=schedules)

#     except Exception as e:
#         print(f"❌ Error in get_filtered_schedules: {e}")
#         return JSONResponse(status_code=500, content={"error": str(e)})


from fastapi import APIRouter
from fastapi.responses import JSONResponse
from firebase_admin import firestore
from pydantic import BaseModel
from typing import Optional, List,  Union 
import requests

router = APIRouter()

# Define the Interval structure properly
class Interval(BaseModel):
    value: int
    unit: str

# Full Schedule model
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
    completed: Optional[bool] = None

@router.post("/api/watering-schedule")
def save_schedule(schedule: Schedule):
    try:
        print("📥 Step 1: Backend received watering schedule:")
        print(schedule)

        # Save to Firebase Firestore
        db = firestore.client()
        doc_ref = db.collection("watering_schedules").add(schedule.dict())
        doc_id = doc_ref[1].id
        print(f"✅ Step 2: Schedule saved to Firebase with ID: {doc_id}")

        # Send to ESP32 (replace with your actual ESP IP or fetch from Firestore)
        esp_ip = "192.168.1.100"  # Example; update as needed or fetch dynamically
        esp_url = f"http://{esp_ip}/water-now"

        try:
            print(f"🌐 Step 3: Sending watering schedule to ESP32 at {esp_url}...")
            response = requests.post(esp_url, json=schedule.dict(), timeout=5)

            if response.status_code == 200:
                print("✅ Step 4: ESP32 acknowledged schedule.")
            else:
                print(f"⚠️ Step 4: ESP32 responded with status code: {response.status_code}")

        except requests.exceptions.RequestException as esp_error:
            print(f"❌ Step 4: Failed to send schedule to ESP32: {esp_error}")

        return JSONResponse(content={"status": "success", "id": doc_id})

    except Exception as e:
        print(f"❌ Error during schedule processing: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
