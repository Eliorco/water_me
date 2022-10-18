import requests


def get_weather_by_url(url, params=None):
    try:
        resp = requests.get(url, params)
        if resp.status_code != 200:
            raise Exception("Request failed")
    except Exception as e:
        print(e)
        return
    return resp.json()


# if __name__ == '__main__':
#     from dotenv import load_dotenv
#     load_dotenv()
#     import os
#     WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    
#     lat,lon= 32.11067549435341, 34.82060004079175
#     url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric'
#     print(get_weather_by_url(url))