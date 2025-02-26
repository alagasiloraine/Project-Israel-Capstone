# import numpy as np
# import tensorflow as tf
# import pandas as pd
# import pickle

# # Load the trained model and preprocessing details
# model = tf.keras.models.load_model("crop_recommendation_model.h5")
# with open("selected_features.pkl", "rb") as f:
#     selected_features = pickle.load(f)
# with open("label_encoder.pkl", "rb") as f:
#     label_encoder = pickle.load(f)
# with open("power_transformer.pkl", "rb") as f:
#     power_transformer = pickle.load(f)
# with open("robust_scaler.pkl", "rb") as f:
#     robust_scaler = pickle.load(f)

# def preprocess_input(input_data):
#     """Prepare input data for the model."""
#     X = pd.DataFrame([input_data])
#     missing_features = [feat for feat in selected_features if feat not in X.columns]
#     if missing_features:
#         raise ValueError(f"Missing required features: {missing_features}")
#     X_selected = X[selected_features]  # Select relevant features
    
#     # Apply transformations
#     X_transformed = power_transformer.transform(X_selected)
#     X_scaled = robust_scaler.transform(X_transformed)
    
#     return X_scaled

# def predict_crop(input_data):
#     """Predict the best crop for given soil and weather conditions."""
#     try:
#         X = preprocess_input(input_data)
#         predictions = model.predict(X)[0]  # Get prediction probabilities
        
#         # Get top 3 recommended crops
#         top_3_indices = np.argsort(predictions)[-3:][::-1]
#         top_3_crops = [{"crop": label_encoder.inverse_transform([i])[0], "confidence": round(predictions[i] * 100, 2)} for i in top_3_indices]
        
#         return {"recommendations": top_3_crops}
#     except Exception as e:
#         return {"error": str(e)}

# def get_crop_requirements(crop_name):
#     """Returns the weather and water requirements for a given crop."""
    # crop_requirements = {
    #     "Lettuce": {"Temp (°C)": "15-25", "Humidity (%)": "60-80", "Rainfall (mm/month)": "100-150", "Water (L/day)": 1.5},
    #     "Spinach": {"Temp (°C)": "10-24", "Humidity (%)": "50-80", "Rainfall (mm/month)": "80-120", "Water (L/day)": 1.2},
    #     "Pechay": {"Temp (°C)": "18-28", "Humidity (%)": "60-85", "Rainfall (mm/month)": "120-180", "Water (L/day)": 1.8},
    #     "Mustard Greens": {"Temp (°C)": "15-28", "Humidity (%)": "50-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 1.6},
    #     "Kangkong": {"Temp (°C)": "20-32", "Humidity (%)": "60-90", "Rainfall (mm/month)": "150-200", "Water (L/day)": 2.0},
    #     "Malunggay": {"Temp (°C)": "25-35", "Humidity (%)": "40-80", "Rainfall (mm/month)": "50-100", "Water (L/day)": 1.0},
    #     "Tomatoes": {"Temp (°C)": "18-30", "Humidity (%)": "50-70", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.5},
    #     "Cucumber": {"Temp (°C)": "18-30", "Humidity (%)": "50-85", "Rainfall (mm/month)": "80-150", "Water (L/day)": 2.2},
    #     "Bell Peppers": {"Temp (°C)": "18-30", "Humidity (%)": "50-70", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.0},
    #     "Chili Peppers": {"Temp (°C)": "20-30", "Humidity (%)": "40-70", "Rainfall (mm/month)": "40-80", "Water (L/day)": 1.8},
    #     "Eggplant": {"Temp (°C)": "22-30", "Humidity (%)": "50-80", "Rainfall (mm/month)": "60-120", "Water (L/day)": 2.0},
    #     "Ampalaya": {"Temp (°C)": "22-30", "Humidity (%)": "50-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 2.5},
    #     "Okra": {"Temp (°C)": "22-30", "Humidity (%)": "50-80", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.0},
    #     "Patola": {"Temp (°C)": "22-30", "Humidity (%)": "60-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 2.2},
    #     "Upo": {"Temp (°C)": "22-30", "Humidity (%)": "60-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 2.3},
    #     "Kalabasa": {"Temp (°C)": "22-30", "Humidity (%)": "50-85", "Rainfall (mm/month)": "50-120", "Water (L/day)": 2.0},
    #     "Sayote": {"Temp (°C)": "18-28", "Humidity (%)": "60-85", "Rainfall (mm/month)": "100-180", "Water (L/day)": 2.0},
    #     "Carrots": {"Temp (°C)": "15-25", "Humidity (%)": "60-80", "Rainfall (mm/month)": "80-150", "Water (L/day)": 1.5},
    # }
#     return crop_requirements.get(crop_name, {"error": "Crop not found"})




import numpy as np
import tensorflow as tf
import pandas as pd
import joblib

# Load the trained model
model = tf.keras.models.load_model("best_crop_model.keras")

# Load preprocessing tools
selected_features = joblib.load("selected_features.pkl")
label_encoder = joblib.load("label_encoder.pkl")
power_transformer = joblib.load("power_transformer.pkl")
robust_scaler = joblib.load("robust_scaler.pkl")

def generate_engineered_features(X):
    """Generate missing engineered features efficiently."""
    feature_data = {}
    
    for col1 in X.columns:
        for col2 in X.columns:
            if col1 != col2:
                feature_data[f'{col1}_{col2}_ratio'] = X[col1] / (X[col2] + 1e-6)  # Avoid division by zero
                feature_data[f'{col1}_{col2}_product'] = X[col1] * X[col2]
    
    feature_df = pd.DataFrame(feature_data, index=X.index)
    X_new = pd.concat([X, feature_df], axis=1)
    return X_new

def preprocess_input(input_data):
    """Prepare input data for the model."""
    X = pd.DataFrame([input_data])
    X = generate_engineered_features(X)  # Generate missing features
    X_selected = X[selected_features]  # Select relevant features
    X_transformed = power_transformer.transform(X_selected)
    X_scaled = robust_scaler.transform(X_transformed)
    return X_scaled

def predict_crop(input_data):
    """Predict the best crop for given soil and weather conditions."""
    X = preprocess_input(input_data)
    predictions = model.predict(X)[0]  # Get prediction probabilities
    
    # Decode crop labels
    top_3_indices = np.argsort(predictions)[-3:][::-1]
    top_3_crops = [(label_encoder.inverse_transform([i])[0], predictions[i] * 100) for i in top_3_indices]
    
    return top_3_crops

crop_requirements = {
    "Lettuce": {"Temp (°C)": "15-25", "Humidity (%)": "60-80", "Rainfall (mm/month)": "100-150", "Water (L/day)": 1.5},
    "Spinach": {"Temp (°C)": "10-24", "Humidity (%)": "50-80", "Rainfall (mm/month)": "80-120", "Water (L/day)": 1.2},
    "Pechay": {"Temp (°C)": "18-28", "Humidity (%)": "60-85", "Rainfall (mm/month)": "120-180", "Water (L/day)": 1.8},
    "Mustard Greens": {"Temp (°C)": "15-28", "Humidity (%)": "50-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 1.6},
    "Kangkong": {"Temp (°C)": "20-32", "Humidity (%)": "60-90", "Rainfall (mm/month)": "150-200", "Water (L/day)": 2.0},
    "Malunggay": {"Temp (°C)": "25-35", "Humidity (%)": "40-80", "Rainfall (mm/month)": "50-100", "Water (L/day)": 1.0},
    "Tomatoes": {"Temp (°C)": "18-30", "Humidity (%)": "50-70", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.5},
    "Cucumber": {"Temp (°C)": "18-30", "Humidity (%)": "50-85", "Rainfall (mm/month)": "80-150", "Water (L/day)": 2.2},
    "Bell Peppers": {"Temp (°C)": "18-30", "Humidity (%)": "50-70", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.0},
    "Chili Peppers": {"Temp (°C)": "20-30", "Humidity (%)": "40-70", "Rainfall (mm/month)": "40-80", "Water (L/day)": 1.8},
    "Eggplant": {"Temp (°C)": "22-30", "Humidity (%)": "50-80", "Rainfall (mm/month)": "60-120", "Water (L/day)": 2.0},
    "Ampalaya": {"Temp (°C)": "22-30", "Humidity (%)": "50-85", "Rainfall (mm/month)": "100-150", "Water (L/day)": 2.5},
    "Okra": {"Temp (°C)": "22-30", "Humidity (%)": "50-80", "Rainfall (mm/month)": "50-100", "Water (L/day)": 2.0},
    "Carrots": {"Temp (°C)": "15-25", "Humidity (%)": "60-80", "Rainfall (mm/month)": "80-150", "Water (L/day)": 1.5}
}

def get_crop_requirements(crop_name):
    """Returns the weather and water requirements for a given crop."""
    return crop_requirements.get(crop_name, {})

# Sample input data

# Oregano
# sample_data = {
#     'N (ppm)': 45, 'P (ppm)': 10, 'K (ppm)': 30,
#     'Temp (°C)': 28, 'Humidity (%)': 40, 'pH': 5.8,
#     'Rainfall (mm/month)': 60, 'Wind Speed (m/s)': 1.5,
#     'Pressure (hPa)': 1010, 'Cloud Cover (%)': 20
# }

#Oregano
# sample_data = {
#     'N (ppm)': 30, 'P (ppm)': 20, 'K (ppm)': 15,
#     'Temp (°C)': 25, 'Humidity (%)': 60, 'pH': 6.5,
#     'Rainfall (mm/month)': 100, 'Wind Speed (m/s)': 2.0,
#     'Pressure (hPa)': 1013, 'Cloud Cover (%)': 50
# }

# Mustard Greens
# sample_data = {
#     'N (ppm)': 80,  # Higher nitrogen level
#     'P (ppm)': 5,   # Lower phosphorus level
#     'K (ppm)': 45,  # Higher potassium level
#     'Temp (°C)': 15,  # Colder temperature
#     'Humidity (%)': 30,  # Lower humidity
#     'pH': 8.0,  # More alkaline soil
#     'Rainfall (mm/month)': 300,  # Heavy rainfall
#     'Wind Speed (m/s)': 6.5,  # Stronger winds
#     'Pressure (hPa)': 990,  # Lower atmospheric pressure
#     'Cloud Cover (%)': 90  # Mostly cloudy conditions
# }

# Tomatoes
sample_data = {
    'N (ppm)': 10,   # Very low nitrogen
    'P (ppm)': 50,   # High phosphorus
    'K (ppm)': 5,    # Very low potassium
    'Temp (°C)': 45,  # Very hot temperature
    'Humidity (%)': 95,  # Extremely high humidity
    'pH': 4.5,  # Highly acidic soil
    'Rainfall (mm/month)': 0,  # No rainfall (drought conditions)
    'Wind Speed (m/s)': 0.5,  # Almost no wind
    'Pressure (hPa)': 1030,  # High atmospheric pressure
    'Cloud Cover (%)': 0  # Completely clear sky
}

# Get crop recommendation
top_3_recommendations = predict_crop(sample_data)

print("Top 3 Crop Recommendations:")
for rank, (crop, confidence) in enumerate(top_3_recommendations, 1):
    print(f"{rank}. {crop} - {confidence:.2f}%")

# Display details for the top recommendation
top_crop = top_3_recommendations[0][0]
crop_info = get_crop_requirements(top_crop)

print(f"\nBest Recommended Crop: {top_crop}")
print(f"Ideal Temperature: {crop_info.get('Temp (°C)', 'N/A')} °C")
print(f"Ideal Humidity: {crop_info.get('Humidity (%)', 'N/A')}%")
print(f"Ideal Rainfall: {crop_info.get('Rainfall (mm/month)', 'N/A')} mm/month")
print(f"Water Requirement: {crop_info.get('Water (L/day)', 'N/A')} L/day")