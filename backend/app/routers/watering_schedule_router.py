# app/routers/watering_schedule_router.py

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from firebase_admin import firestore
from datetime import datetime, timedelta
import pytz

router = APIRouter()

@router.get("/api/watering-schedules")
def get_filtered_schedules():
    try:
        db = firestore.client()
        ref = db.collection("watering_schedules")
        docs = ref.stream()

        schedules = []
        now = datetime.now(pytz.timezone("Asia/Manila"))  # Use your timezone

        for doc in docs:
            data = doc.to_dict()
            mode = data.get("mode", "weekly")
            raw_datetime = data.get("dateTime", "")
            duration = data.get("duration", 0)
            days = data.get("days", [False]*7)

            # Format and filter logic
            formatted_datetime = ""
            is_valid = False

            try:
                if mode == "one-time":
                    # Format: "Thu, May 2, 06:30 AM"
                    dt = datetime.strptime(raw_datetime, "%a, %b %d, %I:%M %p")
                    dt = pytz.timezone("Asia/Manila").localize(dt)

                    if dt.date() >= now.date():
                        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M")
                        is_valid = True
                else:
                    # Format: "Thu, May 2, 06:30 AM" → "Thu, 06:30"
                    parts = raw_datetime.split(",")
                    if len(parts) >= 3:
                        schedule_day = parts[0].strip()
                        time_part = parts[2].strip().split(" ")[0]
                        formatted_datetime = f"{schedule_day}, {time_part}"

                        # Check if today matches the selected days
                        today_index = now.weekday()  # 0 = Mon, 6 = Sun
                        if mode == "daily":
                            is_valid = True
                        elif mode in ["weekly", "custom"]:
                            if days[today_index]:
                                is_valid = True
            except Exception as e:
                print(f"⚠️ Failed to parse datetime for {doc.id}: {e}")
                continue

            if is_valid:
                schedules.append({
                    "id": doc.id,
                    "dateTime": formatted_datetime,
                    "days": days,
                    "duration": duration,
                    "mode": mode
                })

        return JSONResponse(content=schedules)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
