import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(db_file):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Load data into a DataFrame
    df = pd.read_sql_query('SELECT * FROM weather_data', conn)

    # Plot temperature distribution
    plt.figure(figsize=(10, 6))
    df['Temperature'].hist(bins=20)
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.show()

    # Since 'Date' column is missing, this step is not possible.
    # To visualize temperature over time, you need a date column in the dataset.
    # Here’s how you could visualize the temperature for different cities if you want to:
    plt.figure(figsize=(12, 6))
    for city in df['City'].unique():
        city_data = df[df['City'] == city]
        plt.plot(city_data.index, city_data['Temperature'], marker='o', linestyle='-', label=city)
    plt.title('Temperature for Different Cities')
    plt.xlabel('Index')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    # plt.grid(True)
    # plt.tight_layout()
    plt.show()

    # Close the connection
    conn.close()

if __name__ == "__main__":
    db_file = 'weather_data.db'
    analyze_data(db_file)