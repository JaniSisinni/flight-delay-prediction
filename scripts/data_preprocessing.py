import pandas as pd

def preprocess_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data = data.dropna()
    
    # Feature engineering: add more relevant features
    data['hour'] = pd.to_datetime(data['hour']).dt.hour
    
    # Normalize data
    numeric_cols = ['temperature', 'wind_speed', 'airport_congestion']
    data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].mean()) / data[numeric_cols].std()

    return data

if __name__ == "__main__":
    file_path = 'data\historical_flight_data.csv'
    preprocessed_data = preprocess_data(file_path)
    print(preprocessed_data.head())