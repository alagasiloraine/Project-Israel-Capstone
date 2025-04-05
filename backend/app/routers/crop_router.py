from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from app.ml.crop_ml.prediction_function import predict_crop
from datetime import datetime
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

router = APIRouter()

# Load environment variables
load_dotenv()

# Load Firebase credentials
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
if not FIREBASE_CREDENTIALS:
    raise ValueError("Firebase credentials not found. Set FIREBASE_CREDENTIALS in .env")

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ------------------ Pydantic Models ------------------

class CropInput(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    soilpH: float
    soilMoisture: float
    temperature: float
    humidity: float

class AlternativeCrop(BaseModel):
    crop: str
    confidence: float

class CropPrediction(BaseModel):
    recommendedCrop: str
    successRate: float
    soilCompatibility: float
    growthRate: float
    yieldPotential: float
    alternativeOptions: List[AlternativeCrop]

class CropRecommendationSave(BaseModel):
    recommendedCrop: str
    successRate: float
    soilCompatibility: float
    growthRate: float
    yieldPotential: float
    alternativeOptions: List[AlternativeCrop]

# ------------------ Predict Route ------------------

@router.post("/recommend", response_model=CropPrediction)
async def recommend_crop(data: CropInput):
    try:
        features_dict = {
            "N (ppm)": data.nitrogen,
            "P (ppm)": data.phosphorus,
            "K (ppm)": data.potassium,
            "Temp (°C)": data.temperature,
            "Humidity (%)": data.humidity,
            "pH": data.soilpH,
            "Soil Moisture (%)": data.soilMoisture
        }

        results = predict_crop(features_dict, top_k=3)

        results = sorted(results, key=lambda x: x['confidence'], reverse=True)
        for crop in results:
            crop['confidence'] = round(crop['confidence'] * 100, 2)

        top_crop = results[0]

        return {
            "recommendedCrop": top_crop['crop'],
            "successRate": top_crop['confidence'],
            "soilCompatibility": top_crop.get('soilCompatibility', 0.0),
            "growthRate": top_crop.get('growthRate', 0.0),
            "yieldPotential": top_crop.get('yieldPotential', 0.0),
            "alternativeOptions": [
                {"crop": results[1]['crop'], "confidence": results[1]['confidence']},
                {"crop": results[2]['crop'], "confidence": results[2]['confidence']}
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ------------------ Save Route ------------------

@router.post("/save")
async def save_crop_recommendation(data: CropRecommendationSave):
    try:
        doc_data = data.dict()
        doc_data["timestamp"] = datetime.utcnow().isoformat()

        # Convert alternativeOptions from List[AlternativeCrop] to dicts
        doc_data["alternativeOptions"] = [alt.dict() for alt in data.alternativeOptions]

        doc_data["status"] = "Recommended"

        db.collection("crop_recommendations").add(doc_data)

        return {"message": "Crop recommendation saved to Firebase"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------- History Saved Route ------------------------

@router.get("/recommendations")
async def get_saved_recommendations():
    try:
        docs = db.collection("crop_recommendations") \
                 .order_by("timestamp", direction=firestore.Query.DESCENDING) \
                 .stream()

        recommendations = []
        for doc in docs:
            data = doc.to_dict()
            timestamp = data.get("timestamp")

            if timestamp:
                try:
                    formatted_date = timestamp.strftime("%b %d, %Y, %I:%M %p")
                except Exception:
                    formatted_date = str(timestamp)
            else:
                formatted_date = "N/A"

            recommendations.append({
                "id": doc.id,
                "crop": data.get("recommendedCrop", ""),
                "successRate": data.get("successRate", 0.0),
                "status": data.get("status", "Planted"),  # Optional default
                "date": formatted_date
            })

        return recommendations

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
