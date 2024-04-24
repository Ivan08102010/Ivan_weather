from aiohttp import ClientSession
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather.s import get_weather,get_weather_2
b = '0'

menu = [{'title': 'Главная', 'url_n': 'first'},

        ]



def first(request):
    v = get_weather('Bryansk')
    b = int(v)
    w = get_weather_2('Bryansk')

    return render(request, "weather/first.html", context={'menu': menu, 'v': v, 'b' : b,'w':w})


