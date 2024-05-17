import requests


def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '17bc5822537ddc276d62eb5191385a58'}
        response = requests.get(url,  params=params)
        weather_json = response.json()
        v = weather_json["main"]["temp"] - 273.15
        return int(v)
    except:
        return 0


def get_weather_2(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
        weather_json = requests.get(url=url, params=params).json()
        return (f'{weather_json["weather"][0]["main"]}')
    except:
        return 'Error'
