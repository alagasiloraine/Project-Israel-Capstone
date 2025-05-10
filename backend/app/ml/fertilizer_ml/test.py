<<<<<<< HEAD
import pandas as pd
import numpy as np
import joblib

# Load trained models
fertilizer_model = joblib.load("fertilizer_classifier.pkl")
amount_model = joblib.load("fertilizer_amount_regressor.pkl")
label_encoder = joblib.load("fertilizer_label_encoder.pkl")

# Define feature names (MUST match training dataset)
feature_names = ["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]

# Predefined soil test samples (converted to DataFrame)
test_samples = pd.DataFrame([
    [15, 8, 40, 6.5, 2.0],
    
], columns=feature_names)

# Expected fertilizers (for comparison)
expected_fertilizers = ["Blood Meal", "Chicken Manure", "Bone Meal", "Lime", "Compost"]
expected_amounts = [75, 200, 150, 400, 300]  # kg/ha

# Make predictions
fertilizer_preds = fertilizer_model.predict(test_samples)
amount_preds = amount_model.predict(test_samples)

# Convert predictions back to labels
fertilizer_preds_labels = label_encoder.inverse_transform(fertilizer_preds)

# Print results
print("🔍 Test Predictions:")
for i in range(len(test_samples)):
    print(f"\n🌱 Soil Test {i+1}: {test_samples.iloc[i].to_dict()}")
    print(f"✅ Expected Fertilizer: {expected_fertilizers[i]} ({expected_amounts[i]} kg/ha)")
    print(f"🔮 Predicted Fertilizer: {fertilizer_preds_labels[i]} ({amount_preds[i]:.1f} kg/ha)")


# import pandas as pd
# import joblib

# # Load trained models and scaler
# fertilizer_model = joblib.load("fertilizer_classifier.pkl")
# amount_model = joblib.load("fertilizer_amount_regressor.pkl")
# label_encoder = joblib.load("fertilizer_label_encoder.pkl")
# scaler = joblib.load("scaler.pkl")  # Load the scaler used during training

# # Define feature names (MUST match training dataset)
# feature_names = ["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]

# # Predefined soil test samples (converted to DataFrame)
# test_samples = pd.DataFrame([
#     [15, 8, 40, 6.5, 2.0],
#     [30, 12, 60, 5.5, 1.2],
#     [5, 25, 80, 7.2, 3.5],
#     [40, 5, 20, 4.8, 1.0],
#     [10, 18, 90, 6.0, 4.5],
# ], columns=feature_names)

# # Apply the same scaling as in training (only for "pH" and "Organic Matter (%)")
# test_samples_scaled = test_samples.copy()
# test_samples_scaled[["pH", "Organic Matter (%)"]] = scaler.transform(test_samples_scaled[["pH", "Organic Matter (%)"]])

# # Expected fertilizers (for comparison)
# expected_fertilizers = ["Blood Meal", "Chicken Manure", "Bone Meal", "Lime", "Compost"]
# expected_amounts = [75, 200, 150, 400, 300]  # kg/ha

# # Make predictions
# fertilizer_preds = fertilizer_model.predict(test_samples_scaled)
# amount_preds = amount_model.predict(test_samples_scaled)

# # Convert predictions back to labels
# fertilizer_preds_labels = label_encoder.inverse_transform(fertilizer_preds)

# # Print results
# print("🔍 Test Predictions:")
# for i in range(len(test_samples)):
#     print(f"\n🌱 Soil Test {i+1}: {test_samples.iloc[i].to_dict()}")
#     print(f"✅ Expected Fertilizer: {expected_fertilizers[i]} ({expected_amounts[i]} kg/ha)")
#     print(f"🔮 Predicted Fertilizer: {fertilizer_preds_labels[i]} ({amount_preds[i]:.1f} kg/ha)")
=======
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

def load_models():
    """Load all trained models and encoders"""
    try:
        # Get the directory where this file is located
        current_dir = Path(__file__).parent
        
        # Load models using absolute paths
        type_model = joblib.load(current_dir / "fertilizer_type_classifier.pkl")
        name_model = joblib.load(current_dir / "fertilizer_name_classifier.pkl")
        amount_model = joblib.load(current_dir / "fertilizer_amount_regressor.pkl")
        type_encoder = joblib.load(current_dir / "fertilizer_type_encoder.pkl")
        name_encoder = joblib.load(current_dir / "fertilizer_name_encoder.pkl")
        
        print("✅ All models loaded successfully!")
        return type_model, name_model, amount_model, type_encoder, name_encoder
    except Exception as e:
        print(f"❌ Error loading models: {str(e)}")
        return None

def predict_fertilizer(soil_data, models):
    """
    Make predictions using the trained models
    
    Args:
        soil_data: dict with keys 'N', 'P', 'K', 'pH', 'OM'
        models: tuple of (type_model, name_model, amount_model, type_encoder, name_encoder)
    """
    type_model, name_model, amount_model, type_encoder, name_encoder = models
    
    # Prepare input data
    X = pd.DataFrame({
        "Nitrogen (mg/kg)": [soil_data['N']],
        "Phosphorus (mg/kg)": [soil_data['P']],
        "Potassium (mg/kg)": [soil_data['K']],
        "pH": [soil_data['pH']],
        "Organic Matter (%)": [soil_data['OM']]
    })
    
    # Make predictions
    type_pred = type_model.predict(X)
    name_pred = name_model.predict(X)
    amount_pred = amount_model.predict(X)
    
    # Decode predictions
    fertilizer_type = type_encoder.inverse_transform(type_pred)[0]
    
    # Get valid fertilizer names based on type
    valid_fertilizers = {
        'solid': ['FFJ Fermented Plant', 'FFJ Fermented Juice Plant', 'Vermi Compost', 'Organic Compost', 'Blood Meal'],
        'liquid': ['OHN Calpus', 'Wound Vinegar', 'Calcium Phosphate', 'Fish Emulsion', 'Seaweed Extract']
    }
    
    # Try to get the predicted name
    try:
        fertilizer_name = name_encoder.inverse_transform(name_pred)[0]
        # Verify if the predicted name is valid for the type
        if fertilizer_name not in valid_fertilizers[fertilizer_type]:
            # If not valid, choose a default for that type
            fertilizer_name = valid_fertilizers[fertilizer_type][0]
    except:
        # If any error in prediction, use a default
        fertilizer_name = valid_fertilizers[fertilizer_type][0]
    
    return {
        'type': fertilizer_type,
        'name': fertilizer_name,
        'amount': round(float(amount_pred[0]), 2)
    }

def main():
    # Load models
    models = load_models()
    if models is None:
        return
    
    # Test cases
    test_cases = [
        {
            'name': "Low Nutrient Soil",
            'data': {'N': 10, 'P': 5, 'K': 30, 'pH': 6.5, 'OM': 1.0}
        },
        {
            'name': "Medium Nutrient Soil",
            'data': {'N': 30, 'P': 15, 'K': 60, 'pH': 7.0, 'OM': 2.5}
        },
        {
            'name': "High Nutrient Soil",
            'data': {'N': 50, 'P': 30, 'K': 100, 'pH': 7.5, 'OM': 4.0}
        },
        {
            'name': "Acidic Soil",
            'data': {'N': 20, 'P': 10, 'K': 40, 'pH': 5.0, 'OM': 2.0}
        },
        {
            'name': "Alkaline Soil",
            'data': {'N': 25, 'P': 20, 'K': 70, 'pH': 8.0, 'OM': 3.0}
        }
    ]
    
    # Run predictions
    print("\n🌱 Testing Fertilizer Recommendations:")
    print("-" * 50)
    
    for test_case in test_cases:
        print(f"\nTest Case: {test_case['name']}")
        print("Soil Conditions:")
        for key, value in test_case['data'].items():
            print(f"  {key}: {value}")
        
        result = predict_fertilizer(test_case['data'], models)
        
        print("\nRecommendation:")
        print(f"  Fertilizer Type: {result['type']}")
        print(f"  Fertilizer Name: {result['name']}")
        print(f"  Amount: {result['amount']} units per square meter")
        print("-" * 50)

if __name__ == "__main__":
    main()
>>>>>>> cy
