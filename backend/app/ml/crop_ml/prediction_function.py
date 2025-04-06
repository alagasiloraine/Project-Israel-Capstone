import pandas as pd
import numpy as np
import joblib
import os
import tensorflow as tf
from tensorflow import keras

# Load preprocessing objects
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PREPROCESS_DIR = os.path.join(BASE_DIR, 'preprocessing')
MODEL_DIR = os.path.join(BASE_DIR)

power_transformer = joblib.load(os.path.join(PREPROCESS_DIR, 'power_transformer.joblib'))
robust_scaler = joblib.load(os.path.join(PREPROCESS_DIR, 'robust_scaler.joblib'))
selected_feature_names = np.load(os.path.join(PREPROCESS_DIR, 'selected_feature_names.npy'), allow_pickle=True)
label_classes = np.load(os.path.join(PREPROCESS_DIR, 'label_classes.npy'), allow_pickle=True)

nn_model = keras.models.load_model(os.path.join(MODEL_DIR, 'crop_nn_model.keras'))

try:
    xgb_model = joblib.load(os.path.join(MODEL_DIR, 'crop_xgb_model.joblib'))
    have_xgb = True
except:
    have_xgb = False

try:
    with open(os.path.join(MODEL_DIR, 'best_model.txt'), 'r') as f:
        best_model_type = f.read().strip()
except:
    best_model_type = "nn"


def calculate_soil_compatibility(features):
    # Basic example logic (scale closeness to ideal pH = 6.5, NPK within typical ranges)
    ideal_pH = 6.5
    ideal_npk = {'N (ppm)': 100, 'P (ppm)': 40, 'K (ppm)': 120}

    pH_score = max(0, 1 - abs(features['pH'] - ideal_pH) / 2)  # within 0.0–1.0
    npk_score = np.mean([
        min(1, features['N (ppm)'] / ideal_npk['N (ppm)']),
        min(1, features['P (ppm)'] / ideal_npk['P (ppm)']),
        min(1, features['K (ppm)'] / ideal_npk['K (ppm)']),
    ])
    return round((0.6 * npk_score + 0.4 * pH_score) * 100, 2)


def estimate_growth_rate(temp, humidity):
    # Optimal ranges (as an example)
    optimal_temp = 25
    optimal_humidity = 60

    temp_score = max(0, 1 - abs(temp - optimal_temp) / 15)
    humidity_score = max(0, 1 - abs(humidity - optimal_humidity) / 40)

    return round(((temp_score + humidity_score) / 2) * 100, 2)


def estimate_yield_potential(data):
    """
    Estimate yield potential based on multiple soil and environmental parameters.
    """
    n = data['N (ppm)']
    p = data['P (ppm)']
    k = data['K (ppm)']
    temp = data['Temp (°C)']
    humidity = data['Humidity (%)']
    ph = data['pH']
    moisture = data['Soil Moisture (%)']

    # Normalize scores (range from 0 to 100)
    n_score = min(n / 150, 1.0) * 100
    p_score = min(p / 100, 1.0) * 100
    k_score = min(k / 150, 1.0) * 100

    temp_score = 100 - abs(temp - 25) * 5
    temp_score = max(min(temp_score, 100), 0)

    humidity_score = 100 - abs(humidity - 60) * 2
    humidity_score = max(min(humidity_score, 100), 0)

    ph_score = 100 - abs(ph - 6.5) * 20
    ph_score = max(min(ph_score, 100), 0)

    if moisture < 60:
        moisture_score = (moisture / 60) * 100
    elif moisture > 120:
        moisture_score = max(100 - (moisture - 120) * 0.5, 60)
    else:
        moisture_score = 100

    yield_score = (
        0.2 * n_score +
        0.15 * p_score +
        0.15 * k_score +
        0.15 * temp_score +
        0.1 * humidity_score +
        0.1 * ph_score +
        0.15 * moisture_score
    )

    return round(yield_score, 2)



def predict_crop(features_dict, top_k=3):
    input_df = pd.DataFrame([features_dict])

    base_cols = ['N (ppm)', 'P (ppm)', 'K (ppm)', 'Temp (°C)', 'Humidity (%)', 'pH', 'Soil Moisture (%)']
    for i, col1 in enumerate(base_cols):
        for col2 in base_cols[i+1:]:
            if col1 in input_df.columns and col2 in input_df.columns:
                input_df[f'{col1}_{col2}_ratio'] = input_df[col1] / (input_df[col2] + 1e-6)
                input_df[f'{col1}_{col2}_product'] = input_df[col1] * input_df[col2]

    for feature in selected_feature_names:
        if feature not in input_df.columns:
            input_df[feature] = 0

    input_df = input_df[selected_feature_names]
    input_np = input_df.to_numpy()
    input_transformed = power_transformer.transform(input_np)
    input_scaled = robust_scaler.transform(input_transformed)

    if best_model_type == "nn" or not have_xgb:
        probabilities = nn_model.predict(input_scaled)[0]
    elif best_model_type == "xgb":
        probabilities = xgb_model.predict_proba(input_scaled)[0]
    else:
        nn_probs = nn_model.predict(input_scaled)[0]
        xgb_probs = xgb_model.predict_proba(input_scaled)[0]
        probabilities = (nn_probs + xgb_probs) / 2

    top_indices = np.argsort(probabilities)[-top_k:][::-1]

    top_predictions = []
    for i, idx in enumerate(top_indices):
        prediction = {
            'crop': label_classes[idx],
            'confidence': float(probabilities[idx]),
            'class_idx': int(idx)
        }

        # Only for top-1 crop, calculate extra metrics
        if i == 0:
            prediction['soilCompatibility'] = calculate_soil_compatibility(features_dict)
            prediction['growthRate'] = estimate_growth_rate(
                features_dict['Temp (°C)'], features_dict['Humidity (%)'])
            prediction['yieldPotential'] = estimate_yield_potential(features_dict)

        top_predictions.append(prediction)

    return top_predictions


# ✅ Example test
if __name__ == "__main__":
    test_features = {
        'N (ppm)': 120,
        'P (ppm)': 50,
        'K (ppm)': 130,
        'Temp (°C)': 28,
        'Humidity (%)': 55,
        'pH': 6.2,
        'Soil Moisture (%)': 145
    }

    result = predict_crop(test_features, top_k=3)
    print("\n🌿 Top 3 Crops with Additional Metrics for #1:")
    for i, r in enumerate(result, 1):
        print(f"{i}. {r['crop']} - Confidence: {r['confidence']:.2%}")
        if i == 1:
            print(f"   🔸 Soil Compatibility: {r['soilCompatibility']}%")
            print(f"   🔸 Growth Rate: {r['growthRate']}%")
            print(f"   🔸 Yield Potential: {r['yieldPotential']}%")
