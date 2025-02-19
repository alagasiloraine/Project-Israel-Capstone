import pandas as pd
import numpy as np
import joblib
import os

def load_model():
    """Load the trained model"""
    model_path = os.path.join(os.path.dirname(__file__), "crop_model.joblib")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)

def preprocess_input(input_data):
    """Convert input dictionary to NumPy array for compatibility"""
    try:
        df = pd.DataFrame([input_data])
        return df.to_numpy()  # Convert to NumPy array to match training format
    except Exception as e:
        raise ValueError(f"Error processing input data: {e}")

def test_model():
    """Test the model with various input combinations"""
    try:
        model = load_model()
        print("✅ Model loaded successfully!")

        test_cases = [
            {
                "name": "Optimal conditions for rice",
                "input": {
                    "N": 80.00, "P": 40.00, "K": 40.00,
                    "temperature": 25.00, "humidity": 85.00,
                    "ph": 6.0, "rainfall": 250.00
                }
            },
            {
                "name": "Optimal conditions for wheat",
                "input": {
                    "N": 120.00, "P": 60.00, "K": 50,
                    "temperature": 20, "humidity": 65,
                    "ph": 6.5, "rainfall": 85.00
                }
            }
        ]

        print("\n🚀 Running test cases...")
        print("-" * 50)

        for test_case in test_cases:
            print(f"\n🟢 Test Case: {test_case['name']}")
            print("📌 Input parameters:", test_case['input'])

            input_data = preprocess_input(test_case["input"])
            
            # Get predictions
            prediction = model.predict(input_data)[0]  # Extract single value
            probability = (
                max(model.predict_proba(input_data)[0]) if hasattr(model, "predict_proba") else 1.0
            )  # Use probability if available
            
            # Format output
            result = {"crop": prediction, "probability": probability}
            
            print("\n🔍 Recommendation:")
            print(f"- {result['crop']} (Probability: {result['probability']:.2f})")
            print("-" * 50)

    except Exception as e:
        print(f"❌ Error testing model: {str(e)}")

if __name__ == "__main__":
    test_model()
