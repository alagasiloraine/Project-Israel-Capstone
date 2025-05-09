import os
import sys
from pathlib import Path
from app.ml.crop_ml.prediction_function import predict_crop
from app.ml.fertilizer_ml.test import load_models, predict_fertilizer

def check_models_exist():
    """Check if all required model files exist"""
    base_path = Path(__file__).parent / "fertilizer_ml"
    required_files = [
        "fertilizer_type_classifier.pkl",
        "fertilizer_name_classifier.pkl",
        "fertilizer_amount_regressor.pkl",
        "fertilizer_type_encoder.pkl",
        "fertilizer_name_encoder.pkl"
    ]
    
    missing_files = []
    for file in required_files:
        if not (base_path / file).exists():
            missing_files.append(file)
    
    return missing_files

def get_integrated_recommendation(soil_data):
    """
    Get integrated crop and fertilizer recommendations
    
    Args:
        soil_data: dict with keys:
            - 'N (ppm)': Nitrogen content
            - 'P (ppm)': Phosphorus content
            - 'K (ppm)': Potassium content
            - 'Temp (°C)': Temperature
            - 'Humidity (%)': Humidity
            - 'pH': pH level
            - 'Soil Moisture (%)': Soil moisture
    
    Returns:
        dict containing crop recommendations and fertilizer recommendations for each crop
    """
    try:
        # Check if models exist
        missing_files = check_models_exist()
        if missing_files:
            return {
                "error": "Missing model files",
                "details": f"Please train the fertilizer models first. Missing files: {', '.join(missing_files)}",
                "soil_conditions": soil_data
            }
        
        # Get crop recommendations
        crop_recommendations = predict_crop(soil_data, top_k=3)
        
        # Load fertilizer models
        fertilizer_models = load_models()
        if fertilizer_models is None:
            return {
                "error": "Failed to load fertilizer models",
                "details": "Error loading the trained models. Please ensure models are properly trained.",
                "soil_conditions": soil_data
            }
        
    
    
        # Convert ppm to mg/kg (1 ppm = 1 mg/kg)
        fertilizer_soil_data = {
            'N': soil_data['N (ppm)'],
            'P': soil_data['P (ppm)'],
            'K': soil_data['K (ppm)'],
            'pH': soil_data['pH'],
            'OM': 2.0  # Default value, should be provided in actual data
        }
        
        # Get fertilizer recommendations for each crop
        recommendations = {
            "soil_conditions": soil_data,
            "recommendations": []
        }
        
        for crop_rec in crop_recommendations:
            fertilizer_rec = predict_fertilizer(fertilizer_soil_data, fertilizer_models)
            
            # Calculate adjusted amount based on crop confidence
            base_amount = fertilizer_rec['amount']
            confidence = crop_rec['confidence']
            adjusted_amount = base_amount * (0.5 + 0.5 * confidence)  # Scale amount by confidence
            
            recommendation = {
                "crop": crop_rec['crop'],
                "confidence": crop_rec['confidence'],
                "fertilizer": {
                    "type": fertilizer_rec['type'],
                    "name": fertilizer_rec['name'],
                    "base_amount": base_amount,
                    "adjusted_amount": round(adjusted_amount, 2),
                    "unit": "kg/m²" if fertilizer_rec['type'] == 'solid' else 'L/m²'
                }
            }
            
            # Add additional metrics if available
            if 'soilCompatibility' in crop_rec:
                recommendation.update({
                    "soil_compatibility": crop_rec['soilCompatibility'],
                    "growth_rate": crop_rec['growthRate'],
                    "yield_potential": crop_rec['yieldPotential']
                })
            
            recommendations["recommendations"].append(recommendation)
        
        return recommendations
    
    except Exception as e:
        return {
            "error": "Unexpected error",
            "details": str(e),
            "soil_conditions": soil_data
        }

def print_recommendations(result):
    """Pretty print the recommendations"""
    print("\n🌱 Integrated Crop and Fertilizer Recommendations")
    print("-" * 60)
    
    # Print soil conditions
    print("\nSoil Conditions:")
    for key, value in result["soil_conditions"].items():
        print(f"  {key}: {value}")
    
    # Check for errors
    if "error" in result:
        print(f"\n❌ Error: {result['error']}")
        print(f"Details: {result['details']}")
        print("\n⚠️ Please run the following commands to train the models:")
        print("1. cd backend/app/ml/fertilizer_ml")
        print("2. python train.py")
        return
    
    # Print recommendations
    print("\nTop 3 Recommendations:")
    for i, rec in enumerate(result["recommendations"], 1):
        print(f"\n{i}. Crop: {rec['crop']}")
        print(f"   Confidence: {rec['confidence']:.2%}")
        if 'soil_compatibility' in rec:
            print(f"   Soil Compatibility: {rec['soil_compatibility']}%")
            print(f"   Growth Rate: {rec['growth_rate']}%")
            print(f"   Yield Potential: {rec['yield_potential']}%")
        
        print(f"\n   Recommended Fertilizer:")
        print(f"   - Type: {rec['fertilizer']['type']}")
        print(f"   - Name: {rec['fertilizer']['name']}")
        print(f"   - Amount: {rec['fertilizer']['adjusted_amount']} {rec['fertilizer']['unit']}")
        print("   " + "-" * 40)

if __name__ == "__main__":
    # Test the integrated recommendation system
    test_soil_data = {
        'N (ppm)': 120,
        'P (ppm)': 50,
        'K (ppm)': 130,
        'Temp (°C)': 28,
        'Humidity (%)': 55,
        'pH': 6.2,
        'Soil Moisture (%)': 145
    }
    
    result = get_integrated_recommendation(test_soil_data)
    print_recommendations(result) 