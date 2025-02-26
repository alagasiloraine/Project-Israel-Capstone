# import pandas as pd
# import numpy as np
# import joblib

# # Load trained models
# fertilizer_model = joblib.load("fertilizer_classifier.pkl")
# amount_model = joblib.load("fertilizer_amount_regressor.pkl")
# label_encoder = joblib.load("fertilizer_label_encoder.pkl")

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

# # Expected fertilizers (for comparison)
# expected_fertilizers = ["Blood Meal", "Chicken Manure", "Bone Meal", "Lime", "Compost"]
# expected_amounts = [75, 200, 150, 400, 300]  # kg/ha

# # Make predictions
# fertilizer_preds = fertilizer_model.predict(test_samples)
# amount_preds = amount_model.predict(test_samples)

# # Convert predictions back to labels
# fertilizer_preds_labels = label_encoder.inverse_transform(fertilizer_preds)

# # Print results
# print("🔍 Test Predictions:")
# for i in range(len(test_samples)):
#     print(f"\n🌱 Soil Test {i+1}: {test_samples.iloc[i].to_dict()}")
#     print(f"✅ Expected Fertilizer: {expected_fertilizers[i]} ({expected_amounts[i]} kg/ha)")
#     print(f"🔮 Predicted Fertilizer: {fertilizer_preds_labels[i]} ({amount_preds[i]:.1f} kg/ha)")


import pandas as pd
import joblib

# Load trained models and scaler
fertilizer_model = joblib.load("fertilizer_classifier.pkl")
amount_model = joblib.load("fertilizer_amount_regressor.pkl")
label_encoder = joblib.load("fertilizer_label_encoder.pkl")
scaler = joblib.load("scaler.pkl")  # Load the scaler used during training

# Define feature names (MUST match training dataset)
feature_names = ["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]

# Predefined soil test samples (converted to DataFrame)
test_samples = pd.DataFrame([
    [15, 8, 40, 6.5, 2.0],
    [30, 12, 60, 5.5, 1.2],
    [5, 25, 80, 7.2, 3.5],
    [40, 5, 20, 4.8, 1.0],
    [10, 18, 90, 6.0, 4.5],
], columns=feature_names)

# Apply the same scaling as in training (only for "pH" and "Organic Matter (%)")
test_samples_scaled = test_samples.copy()
test_samples_scaled[["pH", "Organic Matter (%)"]] = scaler.transform(test_samples_scaled[["pH", "Organic Matter (%)"]])

# Expected fertilizers (for comparison)
expected_fertilizers = ["Blood Meal", "Chicken Manure", "Bone Meal", "Lime", "Compost"]
expected_amounts = [75, 200, 150, 400, 300]  # kg/ha

# Make predictions
fertilizer_preds = fertilizer_model.predict(test_samples_scaled)
amount_preds = amount_model.predict(test_samples_scaled)

# Convert predictions back to labels
fertilizer_preds_labels = label_encoder.inverse_transform(fertilizer_preds)

# Print results
print("🔍 Test Predictions:")
for i in range(len(test_samples)):
    print(f"\n🌱 Soil Test {i+1}: {test_samples.iloc[i].to_dict()}")
    print(f"✅ Expected Fertilizer: {expected_fertilizers[i]} ({expected_amounts[i]} kg/ha)")
    print(f"🔮 Predicted Fertilizer: {fertilizer_preds_labels[i]} ({amount_preds[i]:.1f} kg/ha)")
