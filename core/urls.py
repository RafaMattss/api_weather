#urls.py
from pyexpat import ParserCreate
from django.urls import path
from weather.views import *
from user.views import *

urlpatterns = [
    path('', WeatherView.as_view(), name='Weather View'),
    path('generate', WeatherGenerate.as_view(), name='Weather Generate'),
    path('reset', WeatherReset.as_view(), name= "Weather Reset"),
    path('insert', WeatherInsert.as_view(), name= "Weather Insert"),
    path('delete/<id>', WeatherDelete.as_view(), name="Weather Delete"),
    path('edit/<id>', WeatherEdit.as_view(), name="Weather Edit"),
    path('filter', WeatherFilter.as_view(), name="Weather Filter"),
    path('token', UserTokenizer.as_view(), name="User Token")
]