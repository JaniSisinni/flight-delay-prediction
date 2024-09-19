import tensorflow as tf
from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split

def train_model(data_path):
    # Load dataset using the data_path parameter
    data = pd.read_csv(data_path)
    
    # Define features and target variable
    X = data[['temperature', 'wind_speed', 'airport_congestion', 'hour']]
    y = data['delay_time']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build the model
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    # Train the model
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

    # Save the trained model
    model.save('models\\flight_delay_model.h5')

if __name__ == "__main__":
    train_model('data\historical_flight_data.csv') 
