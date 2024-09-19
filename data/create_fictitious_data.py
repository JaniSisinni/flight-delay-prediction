import pandas as pd
import random
import datetime

def generate_random_flight_data(num_rows=10000):
    """Generates random flight data.

    Args:
        num_rows: Number of rows to generate.

    Returns:
        pandas.DataFrame: Generated flight data.
    """

    # Fictional data for values
    airlines = ["SkyHigh Airways", "JetStream Airlines", "CloudNine Aviation", "EagleFly Express", "BlueHorizon Airlines", "Sunset Skies Air"]
    airports = ["JFK", "LHR", "NRT", "CDG", "SYD", "HND", "ORD", "DXB", "LAX", "HKG", "AMS", "FRA", "SFO", "CPT", "GRU", "SCL"]
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Foggy", "Stormy", "Hazy", "Icy", "Hot", "Cold"]
    congestion_levels = ["Low", "Medium", "High","Severe"]

    # Generate random departure times 
    departure_times = [datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 365), 
                                                                    hours=random.randint(0, 23), 
                                                                    minutes=random.randint(0, 59)) 
                       for _ in range(num_rows)]
    
    # Generate arrival times based on departure times
    arrival_times = [departure_time + datetime.timedelta(hours=random.randint(1, 5)) for departure_time in departure_times]

    # Generate random data
    data = {
        "flight_id": range(1, num_rows + 1),
        "departure_time": departure_times,
        "arrival_time": arrival_times,
        "airline": [random.choice(airlines) for _ in range(num_rows)],
        "origin_airport": [random.choice(airports) for _ in range(num_rows)],
        "destination_airport": [random.choice(airports) for _ in range(num_rows)],
        "weather_condition": [random.choice(weather_conditions) for _ in range(num_rows)],
        "airport_congestion": [random.choice(congestion_levels) for _ in range(num_rows)],
        "delay_time": [random.randint(0, 120) for _ in range(num_rows)],
        "temperature": [random.randint(-10, 40) for _ in range(num_rows)],  # Random temperature in °C
        "wind_speed": [random.randint(0, 50) for _ in range(num_rows)],  # Random wind speed in km/h
        "hour": [departure_time.hour for departure_time in departure_times],  # Extract hour from departure time
        "passengers": [random.randint(170, 390) for _ in range(num_rows)]  # Random number of passengers
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Convert datetime columns to strings for CSV
    df["departure_time"] = df["departure_time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["arrival_time"] = df["arrival_time"].dt.strftime("%Y-%m-%d %H:%M:%S")

    return df

# Generate 10,000 rows of data
df = generate_random_flight_data(10000)

# Save to CSV
df.to_csv("historical_flight_data.csv", index=False)
