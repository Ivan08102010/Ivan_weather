from django.urls import path
from weather.views import *
from weather import views
urlpatterns = [
    path('',first,name = 'first'),
    path('',city_base,name = 'city_b'),
    path('city/<int:city_id>/', citis, name='city'),
]
