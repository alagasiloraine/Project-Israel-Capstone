import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from crop_model import CropRecommendationModel
import joblib

def train_crop_model(data_path):
    """
    Train the crop recommendation model and evaluate its performance.
    """
    print("Starting model training...")
    
    # Initialize the model
    model = CropRecommendationModel()
    
    # Prepare the data
    print("Preparing data...")
    df = pd.read_csv(data_path)
    if 'crop' not in df.columns:
        print("Error: The dataset must contain a 'crop' column as the target variable.")
        return
    
    X = df.drop(columns=['crop'])
    y = df['crop']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    print("Training model...")
    model.train(X_train, y_train)
    
    # Save the model
    model_path = os.path.join(os.getcwd(), "crop_model.pkl")
    print("Saving model...")
    joblib.dump(model, model_path)
    if os.path.exists(model_path):
        print("Model saved successfully!")
    else:
        print("Error saving model!")
        return
    
    # Evaluate the model
    print("\nEvaluating model performance...")
    
    # Make predictions on test set
    test_data = X_test.to_dict('records')
    predictions = []
    true_labels = y_test.tolist()
    
    for data in test_data:
        try:
            pred = model.predict(data)
            if isinstance(pred, list) and len(pred) > 0 and 'crop' in pred[0]:
                predictions.append(pred[0]['crop'])
            else:
                predictions.append("Unknown")
        except Exception as e:
            print(f"Prediction error: {e}")
            predictions.append("Unknown")
    
    # Calculate and print metrics
    accuracy = accuracy_score(true_labels, predictions)
    print(f"\nModel Accuracy: {accuracy:.2f}")
    
    print("\nDetailed Classification Report:")
    print(classification_report(true_labels, predictions, zero_division=0))
    
    # Print example predictions
    print("\nExample Predictions:")
    for i in range(min(5, len(test_data))):
        pred = model.predict(test_data[i])
        print(f"\nInput: {test_data[i]}")
        print("Recommendations:")
        for p in pred:
            print(f"- {p['crop']} (Probability: {p['probability']:.2f})")

if __name__ == "__main__":
    # Get the absolute path to the data directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    data_path = os.path.join(data_dir, "Crop_recommendation.csv")
    
    # Create data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    # Check if dataset exists
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        print("Please place the Crop_recommendation.csv file in the data directory")
        exit(1)
    
    # Train the model
    train_crop_model(data_path)
