# import requests
#
#
# def get_weather(city):
#     url = f'http://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'APPID': '17bc5822537ddc276d62eb5191385a58'}
#     response = requests.get(url,  params=params)
#     weather_json = response.json()
#     #print(weather_json)
#     v = weather_json["main"]["temp"] - 273.15
#     return str(int(v))


#print(get_weather('Bryansk'))
# http://api.openweathermap.org/data/2.5/weather?q=Bryansk&APPID=17bc5822537ddc276d62eb5191385a58