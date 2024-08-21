import sqlite3
import pandas as pd

def load_data_to_sqlite(csv_file, db_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table (if not exists)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            City TEXT,
            Temperature REAL,
            Feels_Like REAL,
            Weather TEXT,
            Humidity INTEGER,
            Wind_Speed REAL,
            Visibility INTEGER,
            PRIMARY KEY (City)  -- Ensure unique entries for each city
        )
    ''')

    # Load data into the table (upsert to handle existing entries)
    df.to_sql('weather_data', conn, if_exists='replace', index=False)

    # Commit and close
    conn.commit()
    conn.close()
    print(f"Data loaded into {db_file}")

if __name__ == "__main__":
    csv_file = 'weather_data.csv'  # Path to your CSV file
    db_file = 'weather_data.db'    # SQLite database file
    load_data_to_sqlite(csv_file, db_file)
