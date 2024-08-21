import requests

def fetch_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    api_key = '4c25f30130e0e8f4bd0fc538f69e1a59'  # Replace with your API key
    city = 'New York'  # Example city
    data = fetch_weather_data(city, api_key)
    print(data)  # For debugging
