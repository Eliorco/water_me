from dataclasses import dataclass
import requests
from requests import Response
import json

@dataclass
class WeatherApp:
    location: tuple[float,float]

    @staticmethod
    def get_weather_by_url(url, params=None):
        try:
            resp = requests.get(url, params)
            if resp.status_code != 200:
                raise Exception("Request failed")
        except Exception as e:
            print(e)
            return
        return resp.json()

    @staticmethod
    def parse_api_call(response):
        # resp = response.json()
        # print(resp)
        return {'current_temp': response['main']['temp'],
                'location': response['name']}

if __name__ == '__main__':
    lat,lon= 32.11067549435341, 34.82060004079175
    w = WeatherApp((lat,lon))
    WEATHER_API_KEY='86acf783a1595a217ad866af2f98b3a6'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric'
    print(w.parse_api_call(w.get_weather_by_url(url)))