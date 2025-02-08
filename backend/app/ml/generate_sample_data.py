import pandas as pd
import numpy as np
import os

def generate_sample_data(n_samples=1000):
    """
    Generate synthetic data for crop recommendation
    """
    # Define crops and their optimal growing conditions
    crops = {
        'rice': {'N': (60, 100), 'P': (30, 50), 'K': (30, 50), 
                'temperature': (20, 30), 'humidity': (80, 95), 
                'ph': (5.5, 6.5), 'rainfall': (200, 300)},
        'wheat': {'N': (100, 140), 'P': (50, 70), 'K': (40, 60), 
                 'temperature': (15, 25), 'humidity': (60, 70), 
                 'ph': (6.0, 7.0), 'rainfall': (75, 100)},
        'corn': {'N': (120, 160), 'P': (60, 80), 'K': (50, 70), 
                'temperature': (20, 30), 'humidity': (65, 75), 
                'ph': (5.5, 7.0), 'rainfall': (200, 300)},
        'sugarcane': {'N': (140, 180), 'P': (70, 90), 'K': (60, 80), 
                     'temperature': (25, 35), 'humidity': (70, 85), 
                     'ph': (6.0, 7.5), 'rainfall': (150, 200)},
        'cotton': {'N': (80, 120), 'P': (40, 60), 'K': (35, 55), 
                  'temperature': (22, 32), 'humidity': (50, 65), 
                  'ph': (5.5, 7.0), 'rainfall': (100, 150)}
    }
    
    data = []
    for _ in range(n_samples):
        # Randomly select a crop
        crop = np.random.choice(list(crops.keys()))
        crop_conditions = crops[crop]
        
        # Generate values within the optimal range with some noise
        sample = {
            'N': np.random.uniform(*crop_conditions['N']),
            'P': np.random.uniform(*crop_conditions['P']),
            'K': np.random.uniform(*crop_conditions['K']),
            'temperature': np.random.uniform(*crop_conditions['temperature']),
            'humidity': np.random.uniform(*crop_conditions['humidity']),
            'ph': np.random.uniform(*crop_conditions['ph']),
            'rainfall': np.random.uniform(*crop_conditions['rainfall']),
            'label': crop
        }
        
        # Add some noise to make the data more realistic
        for key in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']:
            noise = np.random.normal(0, (crop_conditions[key][1] - crop_conditions[key][0]) * 0.1)
            sample[key] += noise
        
        data.append(sample)
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate sample data
    print("Generating sample data...")
    df = generate_sample_data(1000)
    
    # Create data directory if it doesn't exist
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Save the data
    output_path = os.path.join(data_dir, "Crop_recommendation.csv")
    df.to_csv(output_path, index=False)
    print(f"Sample data saved to {output_path}")
    
    # Display some statistics
    print("\nDataset Statistics:")
    print(f"Number of samples: {len(df)}")
    print("\nCrop distribution:")
    print(df['label'].value_counts())
    print("\nFeature ranges:")
    for column in df.columns:
        if column != 'label':
            print(f"{column}:")
            print(f"  Min: {df[column].min():.2f}")
            print(f"  Max: {df[column].max():.2f}")
            print(f"  Mean: {df[column].mean():.2f}")
            print()
