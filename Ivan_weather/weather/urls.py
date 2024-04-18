from django.urls import path
from weather.views import *
from weather import views
urlpatterns = [
    path('',first,name = 'first'),
]