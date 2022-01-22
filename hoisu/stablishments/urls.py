from django.urls import path, include
from .views import home, register, login

from rest_framework import routers


urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('register', register, name="register")
]