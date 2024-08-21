import pandas as pd
from data_extraction import fetch_weather_data

def transform_and_save_weather_data(cities, api_key, output_file):
    all_data = []
    
    for city in cities:
        weather_data = fetch_weather_data(city, api_key)
        
        if weather_data:
            data = {
                'City': weather_data.get('name'),
                'Temperature': weather_data['main'].get('temp'),
                'Feels Like': weather_data['main'].get('feels_like'),
                'Weather': weather_data['weather'][0].get('description'),
                'Humidity': weather_data['main'].get('humidity'),
                'Wind Speed': weather_data['wind'].get('speed'),
                'Visibility': weather_data.get('visibility')
            }
            all_data.append(data)
        else:
            print(f"Failed to fetch weather data for {city}")
    
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    else:
        print("No data to save")

if __name__ == "__main__":
    api_key = '4c25f30130e0e8f4bd0fc538f69e1a59'
    cities = ['New York', 'Los Angeles', 'Chicago', 'Dallas', 'Miami', 'Albuquerque', 'Boston', 'Charlotte', 'Denver', 'Phoenix', 'Buffalo',
              'San Jose', 'Seattle', 'Ohio', 'Delaware', 'Montgomery', 'Hartford', 'Sacramento', 'Trenton', 'Atlanta', 'Salem', 'Annapolis',
              'Des Moines', 'Indianapolis', 'Baton Rouge', 'Salt Lake City', 'Richmond', 'Montpelier', 'Providence', 'Harrisburg', 'Columbia',
              'Richmond', 'Olympia', 'Jackson', 'Saint Paul', 'Lansing', 'Cheyenne', 'Madison', 'Charleston', 'Montpelier', 'Pierre', 'Springfield',
              'Honolulu', 'Topeka', 'Frankfort', 'Augusta', 'Nashville', 'Oklahoma City', 'Concord', 'Lincoln', 'Helena', 'Juneau', 'Little Rock']
    output_file = 'weather_data.csv'
    transform_and_save_weather_data(cities, api_key, output_file)
