# import pandas as pd
# import numpy as np
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.preprocessing import LabelEncoder
# from sklearn.metrics import accuracy_score, mean_absolute_error

# # Load dataset
# df = pd.read_csv("soil_fertilizer_dataset.csv")

# # Encode the categorical target (Fertilizer Type)
# label_encoder = LabelEncoder()
# df["Fertilizer Label"] = label_encoder.fit_transform(df["Recommended Fertilizer"])

# # Features and Targets
# X = df[["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]]
# y_fertilizer = df["Fertilizer Label"]  # Classification target
# y_amount = df["Amount (kg/ha)"]  # Regression target

# # Split data (80% train, 20% test)
# X_train, X_test, y_fert_train, y_fert_test = train_test_split(X, y_fertilizer, test_size=0.2, random_state=42)
# X_train, X_test, y_amt_train, y_amt_test = train_test_split(X, y_amount, test_size=0.2, random_state=42)

# # Train Fertilizer Type Classifier
# fertilizer_model = RandomForestClassifier(n_estimators=100, random_state=42)
# fertilizer_model.fit(X_train, y_fert_train)

# # Train Fertilizer Amount Regressor
# amount_model = RandomForestRegressor(n_estimators=100, random_state=42)
# amount_model.fit(X_train, y_amt_train)

# # Evaluate models
# fertilizer_preds = fertilizer_model.predict(X_test)
# amount_preds = amount_model.predict(X_test)

# fert_accuracy = accuracy_score(y_fert_test, fertilizer_preds)
# amt_error = mean_absolute_error(y_amt_test, amount_preds)

# print(f"Fertilizer Classification Accuracy: {fert_accuracy:.2f}")
# print(f"Fertilizer Amount Prediction MAE: {amt_error:.2f}")

# # Save models
# joblib.dump(fertilizer_model, "fertilizer_classifier.pkl")
# joblib.dump(amount_model, "fertilizer_amount_regressor.pkl")
# joblib.dump(label_encoder, "fertilizer_label_encoder.pkl")

# print("Models trained and saved successfully!")


import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, mean_absolute_error
from imblearn.over_sampling import SMOTE

# Load dataset
df = pd.read_csv("soil_fertilizer_dataset.csv")

# Reset index to prevent indexing issues
df.reset_index(drop=True, inplace=True)

# Encode categorical target (Fertilizer Type)
label_encoder = LabelEncoder()
df["Fertilizer Label"] = label_encoder.fit_transform(df["Recommended Fertilizer"])

# Features and Targets
X = df[["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]]
y_fertilizer = df["Fertilizer Label"]  # Classification target
y_amount = df["Amount (kg/ha)"]  # Regression target

# Normalize pH and Organic Matter
scaler = StandardScaler()
X_scaled = X.copy()
X_scaled[["pH", "Organic Matter (%)"]] = scaler.fit_transform(X_scaled[["pH", "Organic Matter (%)"]])

# Combine features with y_amount to ensure resampling consistency
Xy_combined = X_scaled.copy()
Xy_combined["y_amount"] = y_amount  # Add y_amount to dataset before resampling

# Apply SMOTE to balance classes (on both features and y_amount)
smote = SMOTE(random_state=42)
X_resampled, y_fert_resampled = smote.fit_resample(Xy_combined, y_fertilizer)

# Extract resampled y_amount
y_amt_resampled = X_resampled.pop("y_amount")  # Remove y_amount from features after resampling

# Split data (80% train, 20% test)
X_train, X_test, y_fert_train, y_fert_test = train_test_split(
    X_resampled, y_fert_resampled, test_size=0.2, random_state=42, stratify=y_fert_resampled
)

X_train, X_test, y_amt_train, y_amt_test = train_test_split(
    X_resampled, y_amt_resampled, test_size=0.2, random_state=42
)

# Train Fertilizer Type Classifier
fertilizer_model = RandomForestClassifier(n_estimators=200, random_state=42)
fertilizer_model.fit(X_train, y_fert_train)

# Train Fertilizer Amount Regressor
amount_model = RandomForestRegressor(n_estimators=200, random_state=42)
amount_model.fit(X_train, y_amt_train)

# Evaluate models
fertilizer_preds = fertilizer_model.predict(X_test)
amount_preds = amount_model.predict(X_test)

fert_accuracy = accuracy_score(y_fert_test, fertilizer_preds)
amt_error = mean_absolute_error(y_amt_test, amount_preds)

print(f"🌿 Fertilizer Classification Accuracy: {fert_accuracy:.2f}")
print(f"📏 Fertilizer Amount Prediction MAE: {amt_error:.2f} kg/ha")

# Save models
joblib.dump(fertilizer_model, "fertilizer_classifier.pkl")
joblib.dump(amount_model, "fertilizer_amount_regressor.pkl")
joblib.dump(label_encoder, "fertilizer_label_encoder.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Models trained and saved successfully!")
