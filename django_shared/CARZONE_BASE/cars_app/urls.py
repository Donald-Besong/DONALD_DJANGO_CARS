from django.urls import path
from .views import cars, carservices, search
urlpatterns = [
path('', cars, name='cars'),
path('carservices/', carservices, name='carservices'),
path('search/', search, name='search'),
]
