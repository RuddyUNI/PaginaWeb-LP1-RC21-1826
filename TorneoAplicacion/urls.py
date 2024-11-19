from django.urls import path
from . import views

urlpatterns = [
    path('holamundo/', views.Productos, name='Productos'),
    path('', views.index, name='index'),
]