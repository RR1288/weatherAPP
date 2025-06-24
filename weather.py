import requests
from config import BASE_URL, WEATHER_API_KEY

def get_weather_data(city):
    complete_url = f"{BASE_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        weather_data = response.json()
    else:
        weather_data = {'error': 'City not found'}
    
    return weather_data