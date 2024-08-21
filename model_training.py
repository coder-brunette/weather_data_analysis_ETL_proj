import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_model(db_file):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Load data into a DataFrame
    df = pd.read_sql_query('SELECT * FROM weather_data', conn)

    # Example data preparation
    X = df[['Feels Like', 'Humidity', 'Wind Speed', 'Visibility']]  # Feature columns
    y = df['Temperature'] 

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

    conn.close()

if __name__ == "__main__":
    db_file = 'weather_data.db'
    train_model(db_file)