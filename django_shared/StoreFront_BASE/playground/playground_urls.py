from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('happy/', views.say_happy),
]
