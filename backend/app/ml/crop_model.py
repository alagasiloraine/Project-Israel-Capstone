import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

class CropRecommendationModel:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        self.model_path = os.path.join(os.path.dirname(__file__), 'crop_model.joblib')
        self.scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.joblib')

    def prepare_data(self, data_path):
        """
        Prepare the data for training
        """
        # Load the dataset
        df = pd.read_csv(data_path)
        
        # Separate features and target
        X = df[self.features]
        y = df['label']
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        """
        Train the model
        """
        # Initialize and fit the scaler
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Initialize and train the model
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train_scaled, y_train)

    def save_model(self):
        """
        Save the trained model and scaler
        """
        if self.model is not None and self.scaler is not None:
            joblib.dump(self.model, self.model_path)
            joblib.dump(self.scaler, self.scaler_path)
            return True
        return False

    def load_model(self):
        """
        Load the trained model and scaler
        """
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
            return True
        return False

    def predict(self, input_data):
        """
        Make predictions using the trained model
        input_data: dict with keys ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        """
        if self.model is None or self.scaler is None:
            if not self.load_model():
                raise Exception("Model not trained or loaded")
        
        try:
            # Convert input data to DataFrame with numeric values
            if isinstance(input_data, dict):
                # Convert all values to float
                numeric_input = {k: float(v) for k, v in input_data.items()}
                input_df = pd.DataFrame([numeric_input])
            else:
                input_df = pd.DataFrame(input_data)
            
            # Ensure all required features are present
            missing_features = set(self.features) - set(input_df.columns)
            if missing_features:
                raise ValueError(f"Missing required features: {missing_features}")
            
            # Ensure correct feature order
            input_df = input_df[self.features]
            
            # Scale the input data
            input_scaled = self.scaler.transform(input_df)
            
            # Make prediction
            prediction = self.model.predict(input_scaled)
            
            # Get probability scores for all crops
            probabilities = self.model.predict_proba(input_scaled)[0]
            
            # Get top 3 recommendations with their probabilities
            top_3_idx = np.argsort(probabilities)[-3:][::-1]
            recommendations = [
                {
                    'crop': self.model.classes_[idx],
                    'probability': float(probabilities[idx])
                }
                for idx in top_3_idx
            ]
            
            return recommendations
            
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")
