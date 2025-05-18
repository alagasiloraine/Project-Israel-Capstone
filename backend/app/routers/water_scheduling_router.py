from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from firebase_admin import firestore
from datetime import datetime
import pytz

router = APIRouter()

@router.get("/api/watering-schedules")
def get_filtered_schedules(request: Request):
    try:
        print(f"📡 API Hit: {request.client.host} | User-Agent: {request.headers.get('user-agent')}")
        
        db = firestore.client()
        ref = db.collection("watering_schedules")
        docs = ref.stream()

        schedules = []
        now = datetime.now(pytz.timezone("Asia/Manila"))
        print(f"📅 Current datetime (Asia/Manila): {now}")

        for doc in docs:
            data = doc.to_dict()
            mode = data.get("mode", "weekly")
            raw_datetime = data.get("dateTime", "")
            duration = data.get("duration", 0)
            days = data.get("days", [False]*7)

            print(f"📄 Processing doc ID: {doc.id}")
            print(f"🧩 Mode: {mode} | Raw datetime: {raw_datetime} | Duration: {duration} | Days: {days}")

            formatted_datetime = ""
            is_valid = False

            try:
                if mode == "one-time":
                    dt = datetime.strptime(raw_datetime, "%a, %b %d, %I:%M %p")
                    dt = pytz.timezone("Asia/Manila").localize(dt)
                    print(f"🕒 Parsed one-time datetime: {dt}")

                    if dt >= now:
                        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M")
                        is_valid = True
                    else:
                        print("⏭️ Skipped: one-time schedule is in the past.")
                else:
                    parts = raw_datetime.split(",")
                    if len(parts) >= 3:
                        schedule_day = parts[0].strip()
                        time_part = parts[2].strip().split(" ")[0]
                        formatted_datetime = f"{schedule_day}, {time_part}"

                        today_index = now.weekday()
                        print(f"📆 Today is weekday index {today_index}")

                        if mode == "daily":
                            is_valid = True
                        elif days[today_index]:
                            is_valid = True
                        else:
                            print("⏭️ Skipped: schedule is not set for today.")
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

        if schedules:
            print(f"✅ {len(schedules)} valid schedule(s) ready to be sent.")
        else:
            print("📦 Returning 0 valid schedules.")

        return JSONResponse(content=schedules)

    except Exception as e:
        print(f"❌ Error in get_filtered_schedules: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})