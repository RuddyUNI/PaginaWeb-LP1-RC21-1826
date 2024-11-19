from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.

def Productos(request):
    return HttpResponse("<h1>Nuestra primera vista!</h1>")


def index(request):
    return render(request, 'index.html')