import matplotlib.pyplot as plt
import pandas as pd

def plot_delay_trends(file_path):
    data = pd.read_csv(file_path)
    
    # Plot 1: Delay Time over Departure Time
    plt.figure(figsize=(12, 6))
    plt.plot(data['departure_time'], data['delay_time'], label='Delay Time', color='b')
    plt.title('Flight Delay Trends Over Time')
    plt.xlabel('Departure Time')
    plt.ylabel('Delay (minutes)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 2: Delay Time by Weather Condition
    plt.figure(figsize=(12, 6))
    data.groupby('weather_condition')['delay_time'].mean().plot(kind='bar', color='g')
    plt.title('Average Delay Time by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Delay (minutes)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 3: Delay Time by Airport Congestion
    plt.figure(figsize=(12, 6))
    data.groupby('airport_congestion')['delay_time'].mean().plot(kind='bar', color='r')
    plt.title('Average Delay Time by Airport Congestion')
    plt.xlabel('Airport Congestion Level')
    plt.ylabel('Average Delay (minutes)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 4: Delay Time vs Temperature
    plt.figure(figsize=(12, 6))
    plt.scatter(data['temperature'], data['delay_time'], alpha=0.5, color='c')
    plt.title('Delay Time vs Temperature')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Delay (minutes)')
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 5: Delay Time vs Wind Speed
    plt.figure(figsize=(12, 6))
    plt.scatter(data['wind_speed'], data['delay_time'], alpha=0.5, color='m')
    plt.title('Delay Time vs Wind Speed')
    plt.xlabel('Wind Speed (km/h)')
    plt.ylabel('Delay (minutes)')
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 6: Delay Time by Airline
    plt.figure(figsize=(12, 6))
    data.groupby('airline')['delay_time'].mean().plot(kind='bar', color='y')
    plt.title('Average Delay Time by Airline')
    plt.xlabel('Airline')
    plt.ylabel('Average Delay (minutes)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 7: Delay Time Distribution
    plt.figure(figsize=(12, 6))
    plt.hist(data['delay_time'], bins=30, color='orange', edgecolor='black')
    plt.title('Distribution of Delay Times')
    plt.xlabel('Delay (minutes)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()  # Show the plot

    # Plot 8: Passengers vs Delay Time
    plt.figure(figsize=(12, 6))
    plt.scatter(data['passengers'], data['delay_time'], alpha=0.5, color='purple')
    plt.title('Delay Time vs Number of Passengers')
    plt.xlabel('Number of Passengers')
    plt.ylabel('Delay (minutes)')
    plt.tight_layout()
    plt.show()  # Show the plot

if __name__ == "__main__":
    plot_delay_trends('data/historical_flight_data.csv')
