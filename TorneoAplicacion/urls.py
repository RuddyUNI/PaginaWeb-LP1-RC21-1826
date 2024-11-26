from django.urls import path
from . import views

urlpatterns = [
    path('Productos/', views.Productos, name='Productos'),
    path('', views.index, name='index'),
]