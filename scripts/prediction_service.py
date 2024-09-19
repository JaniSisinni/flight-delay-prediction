import tensorflow as tf
import pandas as pd

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_delay(model, new_data):
    prediction = model.predict(new_data)
    return prediction

if __name__ == "__main__":
    model = load_model('models\\flight_delay_model.h5')
    new_data = pd.DataFrame({
        'temperature': [25],
        'wind_speed': [10],
        'airport_congestion': [5],
        'hour': [14]
    })
    predicted_delay = predict_delay(model, new_data)
    print(f"Predicted delay: {predicted_delay[0][0]} minutes")