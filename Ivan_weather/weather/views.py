from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

menu = [{'title' : 'Главная' , 'url_n' : 'first'},

]
def first (request):
    return render(request, "weather/first.html", context={'menu': menu})
