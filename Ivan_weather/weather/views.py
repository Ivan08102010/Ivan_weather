from aiohttp import ClientSession
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather.s import get_weather,get_weather_2
b = '0'

menu = [{'title': 'Главная', 'url_n': 'first'},
        {'title': 'Города', 'url_n': 'city_b'}
        ]
def first(request):
    v = get_weather('Bryansk')
    b = int(v)
    w = get_weather_2('Bryansk')

    return render(request, "weather/first.html", context={'menu': menu, 'v': v, 'b' : b,'w':w})

def city_base(request):
    if request.GET:
        print(request.GET)
        city = request.GET['filed_text']
        print(city)
        vvod = 1
        v = get_weather(city)
        b = int(v)
        w = get_weather_2(city)
    else:
        city = '0'
        vvod = 0
        v = '0'
        b = 0
        w = '0'

    return render(request, "weather/city_base.html", context={'menu': menu, 'b' : b,'w':w,"vvod":vvod,'city':city})



