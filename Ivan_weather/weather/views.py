from aiohttp import ClientSession
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather.s import get_weather

menu = [{'title': 'Главная', 'url_n': 'first'},

        ]



def first(request):
    v = get_weather('Bryansk')
    print(v)
    return render(request, "weather/first.html", context={'menu': menu, 'v': v})
