from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.template import loader
from .models import productos

# Create your views here.

def Productos(request):
    #return HttpResponse("<h1>Nuestra primera vista!</h1>")
    misProductos = productos.objects.all().values()
    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    return render(request, 'index.html')