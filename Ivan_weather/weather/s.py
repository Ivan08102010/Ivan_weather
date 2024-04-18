# import asyncio
# import time
# from pprint import pprint
#
# from aiohttp import ClientSession
#
#
# async def get_weather(city):
#     with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             v = weather_json["main"]["temp"] - 273.15
#             return v
#
#
# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     for task in tasks:
#         await task
#
#
# cities = ['Bryansk']
# if __name__ == '__main__':
#     asyncio.run(main(cities))
#
# import asyncio
# import time
# from aiohttp import ClientSession
#
#
# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '17bc5822537ddc276d62eb5191385a58'}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             v = weather_json["main"]["temp"] - 273.15
#             return str(int(v))
#
#
# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     results = await asyncio.gather(*tasks)
#
#     for result in results:
#         print(result)
#
#
#
#
# cities = ['Bryansk']
# if __name__ == '__main__':
#     asyncio.run(main(cities))


import requests


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '17bc5822537ddc276d62eb5191385a58'}
    response = requests.get(url,  params=params)
    weather_json = response.json()
    #print(weather_json)
    v = weather_json["main"]["temp"] - 273.15
    return str(int(v))
