from django.urls import path
from weather.views import *
from weather import views
urlpatterns = [
    path('',first,name = 'first'),
    path('weatherCity',City,name = 'City'),
    path('',first,name = 'first'),
]