from django.views import generic
from .models import City, Establishment
from django.shortcuts import get_object_or_404, reverse, redirect, render
from .forms import CityForm, EstablishmentForm, ContactForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import CitySerializer, EstablishmentSerializer
from rest_framework import serializers, viewsets




class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class EstablishmentViewset(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


def home(request):
    return render(request, 'hoisu/home.html')

def login(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["messagge"] = "You are register "
        else:
            data["form"] = form
    return render(request, 'hoisu/login/login.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente ")
            return render(request, 'hoisu/home.html')

        data["form"] = form

    return render(request, 'hoisu/registration/register.html', data)