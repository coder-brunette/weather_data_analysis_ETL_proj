from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('weather_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Create DataFrame from request data
    df = pd.DataFrame([data])
    
    # Ensure columns are in the correct order and format
    required_columns = ['Feels Like', 'Humidity', 'Wind Speed', 'Visibility']
    
    # Add missing columns with default values if needed
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0  # Default value if column is missing

    df = df[required_columns]
    
    # Debug statement
    print("DataFrame before prediction:", df)

    # Predict using the trained model
    predictions = model.predict(df)
    
    # Return prediction as JSON response
    return jsonify({'prediction': predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True)