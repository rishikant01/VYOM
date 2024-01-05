import requests

def get_weather(latitude, longitude):
    base_url = 'https://api.open-meteo.com/weather'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true',
        'daily_weather': 'true',
        'timezone': 'auto',
        'hourly': 'temperature_2m_1h',
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            current_temp = data['current_weather']['temperature_2m']
            description = data['current_weather']['summary']['description']
            return f'Current Temperature: {current_temp}°C, {description}'
        else:
            return f'Error: {data["error"]["message"]}'

    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    
    latitude = 23.165710  # Replace with your city's latitude
    longitude = 79.932358 # Replace with your city's longitude

    result = get_weather(latitude, longitude)
    print(result)
