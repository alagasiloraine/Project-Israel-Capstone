import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler, RobustScaler
from sklearn.metrics import accuracy_score, mean_absolute_error, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline
import warnings
import ast
warnings.filterwarnings('ignore')

# Load dataset
print("Loading dataset...")
df = pd.read_csv("soil_fertilizer_dataset.csv")

# Function to safely extract fertilizer information
def extract_fertilizer_info(recommendation):
    try:
        if isinstance(recommendation, str):
            # Convert string representation of list to actual list
            recommendations = ast.literal_eval(recommendation)
        else:
            recommendations = recommendation
            
        if recommendations and len(recommendations) > 0:
            # Get the first recommendation
            rec = recommendations[0]
            return {
                'type': rec.get('type', 'unknown'),
                'fertilizer': rec.get('fertilizer', 'unknown'),
                'amount': float(rec.get('amount', 0))
            }
        return {'type': 'unknown', 'fertilizer': 'unknown', 'amount': 0.0}
    except Exception as e:
        print(f"Error extracting fertilizer info: {e}")
        return {'type': 'unknown', 'fertilizer': 'unknown', 'amount': 0.0}

# Extract fertilizer information
print("\nExtracting fertilizer information...")
fertilizer_info = df['Fertilizer Recommendations'].apply(extract_fertilizer_info)
df['Fertilizer Type'] = fertilizer_info.apply(lambda x: x['type'])
df['Fertilizer Name'] = fertilizer_info.apply(lambda x: x['fertilizer'])
df['Amount'] = fertilizer_info.apply(lambda x: x['amount'])

# Print unique values and their counts
print("\nUnique Fertilizer Types and counts:")
print(df['Fertilizer Type'].value_counts())

print("\nUnique Fertilizer Names and counts:")
print(df['Fertilizer Name'].value_counts())

print("\nSample Amounts:")
print(df['Amount'].describe())

# Remove rows with unknown values
print("\nRemoving rows with unknown values...")
df = df[df['Fertilizer Type'] != 'unknown']
df = df[df['Fertilizer Name'] != 'unknown']

# Prepare features and targets
X = df[["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]]

# Encode fertilizer type and name
print("\nEncoding fertilizer types and names...")
type_encoder = LabelEncoder()
name_encoder = LabelEncoder()

# Fit and transform the encoders
y_type = type_encoder.fit_transform(df['Fertilizer Type'])
y_name = name_encoder.fit_transform(df['Fertilizer Name'])
y_amount = df['Amount']

# Print encoded values
print("\nFertilizer Type encoding mapping:")
for i, label in enumerate(type_encoder.classes_):
    print(f"{label} -> {i}")

print("\nFertilizer Name encoding mapping:")
for i, label in enumerate(name_encoder.classes_):
    print(f"{label} -> {i}")

# Create preprocessing pipeline
numeric_features = ["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]
preprocessor = ColumnTransformer(
    transformers=[
        ('num', RobustScaler(), numeric_features)
    ])

# Split data
X_train, X_test, y_type_train, y_type_test = train_test_split(
    X, y_type, test_size=0.2, random_state=42, stratify=y_type
)
_, _, y_name_train, y_name_test = train_test_split(
    X, y_name, test_size=0.2, random_state=42, stratify=y_name
)
_, _, y_amount_train, y_amount_test = train_test_split(
    X, y_amount, test_size=0.2, random_state=42
)

# Train Fertilizer Type Classifier
print("\nTraining Fertilizer Type Classifier...")
type_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('sampler', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
])

type_pipeline.fit(X_train, y_type_train)
type_preds = type_pipeline.predict(X_test)
type_accuracy = accuracy_score(y_type_test, type_preds)

print(f"Fertilizer Type Classification Accuracy: {type_accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_type_test, type_preds))

# Train Fertilizer Name Classifier
print("\nTraining Fertilizer Name Classifier...")
name_pipeline = ImbPipeline([
    ('preprocessor', preprocessor),
    ('sampler', SMOTE(random_state=42)),
    ('classifier', GradientBoostingClassifier(n_estimators=200, random_state=42))
])

name_pipeline.fit(X_train, y_name_train)
name_preds = name_pipeline.predict(X_test)
name_accuracy = accuracy_score(y_name_test, name_preds)

print(f"Fertilizer Name Classification Accuracy: {name_accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_name_test, name_preds))

# Train Amount Regressor
print("\nTraining Amount Regressor...")
amount_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=200, random_state=42))
])

amount_pipeline.fit(X_train, y_amount_train)
amount_preds = amount_pipeline.predict(X_test)
amount_mae = mean_absolute_error(y_amount_test, amount_preds)

print(f"Amount Prediction MAE: {amount_mae:.4f}")

# Save models and encoders
print("\nSaving models and encoders...")
joblib.dump(type_pipeline, "fertilizer_type_classifier.pkl")
joblib.dump(name_pipeline, "fertilizer_name_classifier.pkl")
joblib.dump(amount_pipeline, "fertilizer_amount_regressor.pkl")
joblib.dump(type_encoder, "fertilizer_type_encoder.pkl")
joblib.dump(name_encoder, "fertilizer_name_encoder.pkl")

print("\n✅ All models trained and saved successfully!")

# Test the saved models
print("\nTesting saved models...")
test_data = {
    'N (ppm)': 120,
    'P (ppm)': 50,
    'K (ppm)': 130,
    'pH': 6.2,
    'OM': 2.0
}

X_test = pd.DataFrame({
    "Nitrogen (mg/kg)": [test_data['N (ppm)']],
    "Phosphorus (mg/kg)": [test_data['P (ppm)']],
    "Potassium (mg/kg)": [test_data['K (ppm)']],
    "pH": [test_data['pH']],
    "Organic Matter (%)": [test_data['OM']]
})

type_pred = type_pipeline.predict(X_test)
name_pred = name_pipeline.predict(X_test)
amount_pred = amount_pipeline.predict(X_test)

print("\nTest Prediction:")
print(f"Fertilizer Type: {type_encoder.inverse_transform(type_pred)[0]}")
print(f"Fertilizer Name: {name_encoder.inverse_transform(name_pred)[0]}")
print(f"Amount: {amount_pred[0]:.2f}")
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_absolute_error

# Load dataset
df = pd.read_csv("soil_fertilizer_dataset.csv")

# Encode the categorical target (Fertilizer Type)
label_encoder = LabelEncoder()
df["Fertilizer Label"] = label_encoder.fit_transform(df["Recommended Fertilizer"])

# Features and Targets
X = df[["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]]
y_fertilizer = df["Fertilizer Label"]  # Classification target
y_amount = df["Amount (kg/ha)"]  # Regression target

# Split data (80% train, 20% test)
X_train, X_test, y_fert_train, y_fert_test = train_test_split(X, y_fertilizer, test_size=0.2, random_state=42)
X_train, X_test, y_amt_train, y_amt_test = train_test_split(X, y_amount, test_size=0.2, random_state=42)

# Train Fertilizer Type Classifier
fertilizer_model = RandomForestClassifier(n_estimators=100, random_state=42)
fertilizer_model.fit(X_train, y_fert_train)

# Train Fertilizer Amount Regressor
amount_model = RandomForestRegressor(n_estimators=100, random_state=42)
amount_model.fit(X_train, y_amt_train)

# Evaluate models
fertilizer_preds = fertilizer_model.predict(X_test)
amount_preds = amount_model.predict(X_test)

fert_accuracy = accuracy_score(y_fert_test, fertilizer_preds)
amt_error = mean_absolute_error(y_amt_test, amount_preds)

print(f"Fertilizer Classification Accuracy: {fert_accuracy:.2f}")
print(f"Fertilizer Amount Prediction MAE: {amt_error:.2f}")

# Save models
joblib.dump(fertilizer_model, "fertilizer_classifier.pkl")
joblib.dump(amount_model, "fertilizer_amount_regressor.pkl")
joblib.dump(label_encoder, "fertilizer_label_encoder.pkl")

print("Models trained and saved successfully!")


# import pandas as pd
# import numpy as np
# import joblib
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.metrics import accuracy_score, mean_absolute_error
# from imblearn.over_sampling import SMOTE

# # Load dataset
# df = pd.read_csv("soil_fertilizer_dataset.csv")

# # Reset index to prevent indexing issues
# df.reset_index(drop=True, inplace=True)

# # Encode categorical target (Fertilizer Type)
# label_encoder = LabelEncoder()
# df["Fertilizer Label"] = label_encoder.fit_transform(df["Recommended Fertilizer"])

# # Features and Targets
# X = df[["Nitrogen (mg/kg)", "Phosphorus (mg/kg)", "Potassium (mg/kg)", "pH", "Organic Matter (%)"]]
# y_fertilizer = df["Fertilizer Label"]  # Classification target
# y_amount = df["Amount (kg/ha)"]  # Regression target

# # Normalize pH and Organic Matter
# scaler = StandardScaler()
# X_scaled = X.copy()
# X_scaled[["pH", "Organic Matter (%)"]] = scaler.fit_transform(X_scaled[["pH", "Organic Matter (%)"]])

# # Combine features with y_amount to ensure resampling consistency
# Xy_combined = X_scaled.copy()
# Xy_combined["y_amount"] = y_amount  # Add y_amount to dataset before resampling

# # Apply SMOTE to balance classes (on both features and y_amount)
# smote = SMOTE(random_state=42)
# X_resampled, y_fert_resampled = smote.fit_resample(Xy_combined, y_fertilizer)

# # Extract resampled y_amount
# y_amt_resampled = X_resampled.pop("y_amount")  # Remove y_amount from features after resampling

# # Split data (80% train, 20% test)
# X_train, X_test, y_fert_train, y_fert_test = train_test_split(
#     X_resampled, y_fert_resampled, test_size=0.2, random_state=42, stratify=y_fert_resampled
# )

# X_train, X_test, y_amt_train, y_amt_test = train_test_split(
#     X_resampled, y_amt_resampled, test_size=0.2, random_state=42
# )

# # Train Fertilizer Type Classifier
# fertilizer_model = RandomForestClassifier(n_estimators=200, random_state=42)
# fertilizer_model.fit(X_train, y_fert_train)

# # Train Fertilizer Amount Regressor
# amount_model = RandomForestRegressor(n_estimators=200, random_state=42)
# amount_model.fit(X_train, y_amt_train)

# # Evaluate models
# fertilizer_preds = fertilizer_model.predict(X_test)
# amount_preds = amount_model.predict(X_test)

# fert_accuracy = accuracy_score(y_fert_test, fertilizer_preds)
# amt_error = mean_absolute_error(y_amt_test, amount_preds)

# print(f"🌿 Fertilizer Classification Accuracy: {fert_accuracy:.2f}")
# print(f"📏 Fertilizer Amount Prediction MAE: {amt_error:.2f} kg/ha")

# # Save models
# joblib.dump(fertilizer_model, "fertilizer_classifier.pkl")
# joblib.dump(amount_model, "fertilizer_amount_regressor.pkl")
# joblib.dump(label_encoder, "fertilizer_label_encoder.pkl")
# joblib.dump(scaler, "scaler.pkl")

# print("✅ Models trained and saved successfully!")
