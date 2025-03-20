
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import json
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
from dotenv import load_dotenv

# Function to load historical weather data
def load_historical_data(file_path):
    """
    Load historical weather data from CSV file
    
    Args:
        file_path (str): Path to the CSV file containing historical weather data
        
    Returns:
        pd.DataFrame: Processed historical weather data
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Convert date column to datetime (assuming there's a date column)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    else:
        # If no date column exists, try to find it or create one
        date_columns = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
        if date_columns:
            df['date'] = pd.to_datetime(df[date_columns[0]])
        else:
            raise ValueError("No date column found in the CSV file")
    
    # Extract month and day features for seasonality
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_year'] = df['date'].dt.dayofyear
    
    return df

# Function to fetch current weather data from WeatherAPI
def fetch_current_weather(api_key, location):
    """
    Fetch current weather data from WeatherAPI
    
    Args:
        api_key (str): Your WeatherAPI API key
        location (str): Location name (e.g., "Parang,Calapan City,Oriental Mindoro")
        
    Returns:
        dict: Current weather data
    """
    # First, get current weather data
    current_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    current_response = requests.get(current_url)
    
    # Then, get forecast for today to get min/max temps
    forecast_url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=1&aqi=no"
    forecast_response = requests.get(forecast_url)
    
    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_data = current_response.json()
        forecast_data = forecast_response.json()
        
        # Combine the data
        combined_data = {
            'current': current_data['current'],
            'forecast': forecast_data['forecast']['forecastday'][0]
        }
        
        return combined_data
    else:
        raise Exception(f"Failed to fetch data. Current: {current_response.status_code}, Forecast: {forecast_response.status_code}")

# Function to map WeatherAPI data to our desired format
def map_weather_data(weather_data):
    """
    Map WeatherAPI data to our desired format
    
    Args:
        weather_data (dict): Weather data from WeatherAPI
        
    Returns:
        dict: Mapped weather data
    """
    mapped_data = {
        'temperature_max': weather_data['forecast']['day']['maxtemp_c'],
        'temperature_min': weather_data['forecast']['day']['mintemp_c'],
        'rainfall': weather_data['forecast']['day']['totalprecip_mm'],
        'precipitation_hours': weather_data['forecast']['day']['daily_will_it_rain'] * 24 / 100,  # Approximation based on chance of rain
        'wind_speed': weather_data['current']['wind_kph'],
        'cloud_cover': weather_data['current']['cloud'],
        'humidity': weather_data['current']['humidity'],
        'pressure': weather_data['current']['pressure_mb'],
        'snowfall': 0  # Default to 0 since this data might not be available directly
    }
    return mapped_data

# Function to get weather forecast features
def prepare_forecast_features(historical_df, current_weather, days=30):
    """
    Prepare features for weather forecasting
    
    Args:
        historical_df (pd.DataFrame): Historical weather data
        current_weather (dict): Current weather conditions
        days (int): Number of days to forecast
        
    Returns:
        pd.DataFrame: Features for forecasting
    """
    # Get current date
    current_date = datetime.now()
    
    # Create dataframe for forecast dates
    forecast_dates = [current_date + timedelta(days=i) for i in range(1, days+1)]
    forecast_df = pd.DataFrame({'date': forecast_dates})
    
    # Extract features
    forecast_df['month'] = forecast_df['date'].dt.month
    forecast_df['day'] = forecast_df['date'].dt.day
    forecast_df['day_of_year'] = forecast_df['date'].dt.dayofyear
    
    # Map current weather data to our format
    mapped_weather = map_weather_data(current_weather)
    
    # Add current weather as lagged features
    for param in mapped_weather:
        forecast_df[f'prev_{param}'] = mapped_weather[param]
    
    return forecast_df

# Function to train weather forecasting models
def train_forecast_models(historical_df):
    """
    Train models for forecasting weather parameters
    
    Args:
        historical_df (pd.DataFrame): Historical weather data
        
    Returns:
        dict: Trained models for each weather parameter
    """
    # Target weather parameters
    target_columns = [
        'temperature_max', 'temperature_min', 'rainfall', 
        'precipitation_hours', 'snowfall', 'wind_speed', 
        'cloud_cover', 'humidity', 'pressure'
    ]
    
    # Create lagged features for previous day's weather
    for col in target_columns:
        if col in historical_df.columns:
            historical_df[f'prev_{col}'] = historical_df[col].shift(1)
        else:
            print(f"Warning: Column '{col}' not found in historical data. Creating empty column.")
            historical_df[col] = 0  # Create with default values
            historical_df[f'prev_{col}'] = 0
    
    # Drop rows with NaN values
    historical_df = historical_df.dropna()
    
    # Define features (seasonal + previous day's weather)
    features = ['month', 'day', 'day_of_year']
    for col in target_columns:
        features.append(f'prev_{col}')
    
    # Initialize models
    models = {}
    scalers = {}
    
    # Train a model for each target variable
    for target in target_columns:
        # Check if target column exists
        if target not in historical_df.columns:
            print(f"Warning: Column '{target}' not found in historical data. Skipping model training.")
            continue
            
        # Split features and target
        X = historical_df[features]
        y = historical_df[target]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        # Store model and scaler
        models[target] = model
        scalers[target] = scaler
        
        # Evaluate model
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        print(f"Model for {target}: Train R² = {train_score:.4f}, Test R² = {test_score:.4f}")
    
    return models, scalers, features

# Function to make weather forecasts
def forecast_weather(forecast_df, models, scalers, features):
    """
    Generate weather forecasts for the next 30 days
    
    Args:
        forecast_df (pd.DataFrame): Features for forecasting
        models (dict): Trained models for each weather parameter
        scalers (dict): Scalers for each model
        features (list): Feature names
        
    Returns:
        pd.DataFrame: Weather forecasts
    """
    # Make a copy of the forecast dataframe
    results_df = forecast_df.copy()
    
    # Target weather parameters
    target_columns = [
        'temperature_max', 'temperature_min', 'rainfall', 
        'precipitation_hours', 'snowfall', 'wind_speed', 
        'cloud_cover', 'humidity', 'pressure'
    ]
    
    # Initialize missing target columns with zeros
    for target in target_columns:
        if target not in results_df.columns:
            results_df[target] = 0
    
    # Loop through each day and predict weather
    for i in range(len(results_df)):
        row = results_df.iloc[[i]]
        
        # Make predictions for each target
        for target in target_columns:
            if target in models:
                # Ensure all features are present in the row
                feature_values = []
                for feat in features:
                    if feat not in row.columns:
                        row[feat] = 0
                
                X = row[features]
                X_scaled = scalers[target].transform(X)
                prediction = models[target].predict(X_scaled)[0]
                
                # Ensure predictions are reasonable
                if target == 'humidity' or target == 'cloud_cover':
                    prediction = max(0, min(100, prediction))  # Clamp between 0-100%
                elif target == 'precipitation_hours':
                    prediction = max(0, min(24, prediction))  # Clamp between 0-24 hours
                elif 'temperature' in target or target in ['rainfall', 'snowfall', 'wind_speed', 'pressure']:
                    prediction = max(0, prediction)  # Ensure non-negative values
                
                # Store prediction
                results_df.loc[results_df.index[i], target] = prediction
        
        # If not the last day, update lagged features for next day
        if i < len(results_df) - 1:
            for target in target_columns:
                if target in models:
                    results_df.loc[results_df.index[i+1], f'prev_{target}'] = results_df.loc[results_df.index[i], target]
    
    return results_df

# Function to evaluate forecast accuracy (added missing function)
def evaluate_forecast_accuracy(historical_df, models, scalers, features):
    """
    Evaluate the accuracy of forecasting models on historical data
    
    Args:
        historical_df (pd.DataFrame): Historical weather data
        models (dict): Trained models for each weather parameter
        scalers (dict): Scalers for each model
        features (list): Feature names
        
    Returns:
        dict: Accuracy metrics for each target
        pd.DataFrame: Comparison of actual vs. predicted values
    """
    # Target weather parameters
    target_columns = [
        'temperature_max', 'temperature_min', 'rainfall', 
        'precipitation_hours', 'snowfall', 'wind_speed', 
        'cloud_cover', 'humidity', 'pressure'
    ]
    
    # Initialize results
    accuracy_metrics = {}
    comparison_data = []
    
    # Get the most recent 30 days of data for testing
    test_df = historical_df.sort_values('date', ascending=False).head(30).sort_values('date')
    
    # For each target, compare predicted vs actual
    for target in target_columns:
        if target not in models or target not in historical_df.columns:
            continue
            
        predictions = []
        actuals = []
        
        # Prepare data for forecasting
        forecast_data = test_df.copy()
        
        # Ensure all required features are present
        for feat in features:
            if feat not in forecast_data.columns:
                forecast_data[feat] = 0
        
        # Make one-day-ahead predictions for each day in the test period
        for i in range(len(forecast_data)):
            # Get features for current day
            X = forecast_data.iloc[[i]][features]
            
            # Skip if any NaN values
            if X.isna().any().any():
                continue
                
            # Scale features
            X_scaled = scalers[target].transform(X)
            
            # Make prediction
            prediction = models[target].predict(X_scaled)[0]
            
            # Apply constraints
            if target == 'humidity' or target == 'cloud_cover':
                prediction = max(0, min(100, prediction))
            elif target == 'precipitation_hours':
                prediction = max(0, min(24, prediction))
            elif 'temperature' in target or target in ['rainfall', 'snowfall', 'wind_speed', 'pressure']:
                prediction = max(0, prediction)
            
            # Get actual value
            actual = forecast_data.iloc[i][target]
            
            # Skip if actual value is NaN
            if pd.isna(actual):
                continue
                
            # Store prediction and actual
            predictions.append(prediction)
            actuals.append(actual)
            
            # Add to comparison data
            comparison_data.append({
                'date': forecast_data.iloc[i]['date'],
                'target': target,
                'predicted': prediction,
                'actual': actual
            })
            
        # Skip if no valid predictions
        if not predictions or not actuals:
            continue
            
        # Calculate metrics
        mae = mean_absolute_error(actuals, predictions)
        rmse = np.sqrt(mean_squared_error(actuals, predictions))
        r2 = r2_score(actuals, predictions)
        
        # Store metrics
        accuracy_metrics[target] = {
            'mae': mae,
            'rmse': rmse,
            'r2': r2
        }
        
    # Create comparison dataframe
    comparison_df = pd.DataFrame(comparison_data)
    
    return accuracy_metrics, comparison_df

# Function to visualize forecasts
def visualize_forecasts(forecast_results):
    """
    Create visualizations of weather forecasts
    
    Args:
        forecast_results (pd.DataFrame): Weather forecast results
    """
    plt.figure(figsize=(15, 30))
    
    # Temperature max/min forecast
    plt.subplot(9, 1, 1)
    plt.plot(forecast_results['date'], forecast_results['temperature_max'], 'r-', label='Max')
    plt.plot(forecast_results['date'], forecast_results['temperature_min'], 'b-', label='Min')
    plt.title('Temperature Forecast (°C)')
    plt.legend()
    plt.grid(True)
    
    # Rainfall forecast
    plt.subplot(9, 1, 2)
    plt.bar(forecast_results['date'], forecast_results['rainfall'], color='blue', alpha=0.7)
    plt.title('Rainfall Forecast (mm)')
    plt.grid(True)
    
    # Precipitation hours forecast
    plt.subplot(9, 1, 3)
    plt.bar(forecast_results['date'], forecast_results['precipitation_hours'], color='cyan', alpha=0.7)
    plt.title('Precipitation Hours Forecast')
    plt.grid(True)
    
    # Snowfall forecast
    plt.subplot(9, 1, 4)
    plt.bar(forecast_results['date'], forecast_results['snowfall'], color='lightblue', alpha=0.7)
    plt.title('Snowfall Forecast (cm)')
    plt.grid(True)
    
    # Wind speed forecast
    plt.subplot(9, 1, 5)
    plt.plot(forecast_results['date'], forecast_results['wind_speed'], 'g-')
    plt.title('Wind Speed Forecast (km/h)')
    plt.grid(True)
    
    # Cloud cover forecast
    plt.subplot(9, 1, 6)
    plt.plot(forecast_results['date'], forecast_results['cloud_cover'], 'grey')
    plt.title('Cloud Cover Forecast (%)')
    plt.grid(True)
    
    # Humidity forecast
    plt.subplot(9, 1, 7)
    plt.plot(forecast_results['date'], forecast_results['humidity'], 'purple')
    plt.title('Humidity Forecast (%)')
    plt.grid(True)
    
    # Pressure forecast
    plt.subplot(9, 1, 8)
    plt.plot(forecast_results['date'], forecast_results['pressure'], 'y-')
    plt.title('Pressure Forecast (mb)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('weather_forecast.png')
    plt.show()

# Main function to run the weather forecasting
def main():
    load_dotenv()
    # Configuration
    api_key = os.getenv("WEATHER_API_KEY")  # Replace with your actual API key
    location = "Parang,Calapan City,Oriental Mindoro"
    historical_data_path = "dataset.csv"  # Replace with your actual file path
    
    # Load historical data
    print("Loading historical weather data...")
    historical_df = load_historical_data(historical_data_path)
    
    # Fetch current weather data
    print("Fetching current weather data...")
    try:
        current_weather = fetch_current_weather(api_key, location)
        mapped_data = map_weather_data(current_weather)
        print(f"Current data: Max Temp: {mapped_data['temperature_max']}°C, Min Temp: {mapped_data['temperature_min']}°C")
    except Exception as e:
        print(f"Error fetching current weather: {e}")
        return
    
    # Train forecasting models
    print("Training forecasting models...")
    models, scalers, features = train_forecast_models(historical_df)
    
    # Prepare features for forecasting
    print("Preparing forecast features...")
    forecast_df = prepare_forecast_features(historical_df, current_weather)
    
    # Generate forecasts
    print("Generating 30-day weather forecast...")
    forecast_results = forecast_weather(forecast_df, models, scalers, features)
    
    # Evaluate forecast accuracy
    print("Evaluating forecast accuracy...")
    try:
        accuracy_metrics, comparison_df = evaluate_forecast_accuracy(historical_df, models, scalers, features)
        print("\nForecast Accuracy Metrics:")
        for target, metrics in accuracy_metrics.items():
            print(f"{target}: MAE = {metrics['mae']:.2f}, RMSE = {metrics['rmse']:.2f}, R² = {metrics['r2']:.2f}")
    except Exception as e:
        print(f"Warning: Could not evaluate forecast accuracy: {e}")
        accuracy_metrics = {}
        comparison_df = pd.DataFrame()
    
    # Save forecast results to CSV
    forecast_results.to_csv('weather_forecast_results.csv', index=False)
    print("Forecast results saved to 'weather_forecast_results.csv'")
    
    # Visualize forecasts
    print("Creating forecast visualizations...")
    visualize_forecasts(forecast_results)
    
    # Print forecast summary
    print("\nWeather Forecast Summary for Next Week:")
    for i in range(7):
        date = forecast_results['date'].iloc[i].strftime('%Y-%m-%d')
        temp_max = forecast_results['temperature_max'].iloc[i]
        temp_min = forecast_results['temperature_min'].iloc[i]
        rainfall = forecast_results['rainfall'].iloc[i]
        precip_hours = forecast_results['precipitation_hours'].iloc[i]
        
        print(f"{date}: {temp_min:.1f}°C to {temp_max:.1f}°C, {rainfall:.1f}mm rainfall over {precip_hours:.1f} hours")

if __name__ == "__main__":
    main()
