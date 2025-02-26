# import numpy as np
# import pandas as pd
# import tensorflow as tf
# import joblib
# from tensorflow.keras.models import load_model
# from tensorflow.keras import backend as K
# from tensorflow.keras.losses import Loss
# import keras

# # Enable unsafe deserialization for Lambda layers
# keras.config.enable_unsafe_deserialization()

# # Define custom FocalLoss class
# @tf.keras.utils.register_keras_serializable()
# class FocalLoss(Loss):
#     def __init__(self, gamma=2.0, alpha=0.25, **kwargs):
#         super(FocalLoss, self).__init__(**kwargs)
#         self.gamma = gamma
#         self.alpha = alpha

#     def call(self, y_true, y_pred):
#         y_true = tf.convert_to_tensor(y_true, dtype=tf.float32)
#         y_pred = tf.convert_to_tensor(y_pred, dtype=tf.float32)
        
#         epsilon = K.epsilon()
#         y_pred = K.clip(y_pred, epsilon, 1.0 - epsilon)
        
#         cross_entropy = -y_true * K.log(y_pred)
#         weight = self.alpha * K.pow((1 - y_pred), self.gamma)
#         loss = weight * cross_entropy
        
#         return K.mean(loss)

#     def get_config(self):
#         config = super().get_config()
#         config.update({"gamma": self.gamma, "alpha": self.alpha})
#         return config

# # Load the trained model with custom objects
# try:
#     model = load_model('best_crop_model.keras', custom_objects={'FocalLoss': FocalLoss}, safe_mode=False)
# except Exception as e:
#     print(f"Error loading model: {e}")
#     exit()

# # Load label encoder
# try:
#     label_encoder = joblib.load('label_encoder.pkl')
# except FileNotFoundError:
#     print("Error: label_encoder.pkl not found!")
#     exit()

# # Load selected features
# try:
#     selected_features = joblib.load('selected_features.pkl')
# except FileNotFoundError:
#     print("Error: selected_features.pkl not found!")
#     exit()

# # Define test data manually with all required features
# sample_test_data = {
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

# # Ensure all required features are present
# for feature in selected_features:
#     if feature not in sample_test_data:
#         sample_test_data[feature] = 0  # Fill missing features with default value

# # Convert to DataFrame with the correct order (No Scaling)
# test_data = pd.DataFrame([sample_test_data])[selected_features]

# # Ensure data shape matches model input
# if test_data.shape[1] != model.input_shape[1]:
#     print(f"Error: Model expects {model.input_shape[1]} features, but test data has {test_data.shape[1]}.")
#     exit()

# # Make predictions
# predictions = model.predict(test_data)
# predicted_classes = np.argmax(predictions, axis=1)
# predicted_labels = label_encoder.inverse_transform(predicted_classes)

# # Save the predictions
# output = pd.DataFrame({'Predicted Crop': predicted_labels})
# output.to_csv('test_predictions.csv', index=False)

# print("Predictions saved to test_predictions.csv")


import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from tensorflow.keras.losses import Loss
import keras

# Enable unsafe deserialization for Lambda layers
keras.config.enable_unsafe_deserialization()

# Define custom FocalLoss class
@tf.keras.utils.register_keras_serializable()
class FocalLoss(Loss):
    def __init__(self, gamma=2.0, alpha=0.25, **kwargs):
        super(FocalLoss, self).__init__(**kwargs)
        self.gamma = gamma
        self.alpha = alpha

    def call(self, y_true, y_pred):
        y_true = tf.convert_to_tensor(y_true, dtype=tf.float32)
        y_pred = tf.convert_to_tensor(y_pred, dtype=tf.float32)
        
        epsilon = K.epsilon()
        y_pred = K.clip(y_pred, epsilon, 1.0 - epsilon)
        
        cross_entropy = -y_true * K.log(y_pred)
        weight = self.alpha * K.pow((1 - y_pred), self.gamma)
        loss = weight * cross_entropy
        
        return K.mean(loss)

    def get_config(self):
        config = super().get_config()
        config.update({"gamma": self.gamma, "alpha": self.alpha})
        return config

# Load the trained model with custom objects
try:
    model = load_model('best_crop_model.keras', custom_objects={'FocalLoss': FocalLoss}, safe_mode=False)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Load label encoder
try:
    label_encoder = joblib.load('label_encoder.pkl')
except FileNotFoundError:
    print("Error: label_encoder.pkl not found!")
    exit()

# Load selected features
try:
    selected_features = joblib.load('selected_features.pkl')
except FileNotFoundError:
    print("Error: selected_features.pkl not found!")
    exit()

# Define test data manually with all required features
sample_test_data = {
    # 'N': 50, 'P': 30, 'K': 40, 'temperature': 25, 'humidity': 80,
    # 'pH': 6.5, 'rainfall': 100, 'EC': 2.5, 'pressure': 1010, 'wind_speed': 60


    # 'N (ppm)': 80,  # Higher nitrogen level
    # 'P (ppm)': 5,   # Lower phosphorus level
    # 'K (ppm)': 45,  # Higher potassium level
    # 'Temp (°C)': 15,  # Colder temperature
    # 'Humidity (%)': 30,  # Lower humidity
    # 'pH': 8.0,  # More alkaline soil
    # 'Rainfall (mm/month)': 300,  # Heavy rainfall
    # 'Wind Speed (m/s)': 6.5,  # Stronger winds
    # 'Pressure (hPa)': 990,  # Lower atmospheric pressure
    # 'Cloud Cover (%)': 90  # Mostly cloudy conditions

    # 'N (ppm)': 30, 'P (ppm)': 20, 'K (ppm)': 15,
    # 'Temp (°C)': 25, 'Humidity (%)': 60, 'pH': 6.5,
    # 'Rainfall (mm/month)': 100, 'Wind Speed (m/s)': 2.0,
    # 'Pressure (hPa)': 1013, 'Cloud Cover (%)': 50

    # 'N (ppm)': 10,   # Very low nitrogen
    # 'P (ppm)': 50,   # High phosphorus
    # 'K (ppm)': 5,    # Very low potassium
    # 'Temp (°C)': 45,  # Very hot temperature
    # 'Humidity (%)': 95,  # Extremely high humidity
    # 'pH': 4.5,  # Highly acidic soil
    # 'Rainfall (mm/month)': 0,  # No rainfall (drought conditions)
    # 'Wind Speed (m/s)': 0.5,  # Almost no wind
    # 'Pressure (hPa)': 1030,  # High atmospheric pressure
    # 'Cloud Cover (%)': 0  # Completely clear sky

}

# Ensure all required features are present
for feature in selected_features:
    if feature not in sample_test_data:
        sample_test_data[feature] = 0  # Fill missing features with default value

# Convert to DataFrame with the correct order (No Scaling)
test_data = pd.DataFrame([sample_test_data])[selected_features]

# Ensure data shape matches model input
if test_data.shape[1] != model.input_shape[1]:
    print(f"Error: Model expects {model.input_shape[1]} features, but test data has {test_data.shape[1]}.")
    exit()

# Make predictions
predictions = model.predict(test_data)
top_3_indices = np.argsort(predictions[0])[::-1][:3]  # Get top 3 indices
top_3_crops = label_encoder.inverse_transform(top_3_indices)  # Convert to crop names
top_3_scores = predictions[0][top_3_indices]  # Get confidence scores

# Crop requirements dictionary
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

# Print top 3 predicted crops
print("\nTop 3 Recommended Crops:")
for i, (crop, score) in enumerate(zip(top_3_crops, top_3_scores), start=1):
    print(f"{i}. {crop} (Confidence: {score:.2%})")

# Get requirements for the top 1 crop
top_crop = top_3_crops[0]
if top_crop in crop_requirements:
    print("\nTop 1 Crop Requirements:")
    for key, value in crop_requirements[top_crop].items():
        print(f"- {key}: {value}")
else:
    print("\nNo stored requirements for the top crop.")

