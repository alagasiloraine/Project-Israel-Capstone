from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.crop_schema import CropInput, CropPrediction
from ..ml.crop_model import CropRecommendationModel

router = APIRouter()
model = CropRecommendationModel()

@router.post("/predict", response_model=List[CropPrediction])
async def predict_crop(input_data: CropInput):
    try:
        # Convert input data to dictionary
        input_dict = input_data.model_dump()
        
        # Get predictions
        predictions = model.predict(input_dict)
        
        return predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
