from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('vistaDos',views.vista2)  # ([Nombre Vista], views.[Nombre de la funcion en views.py])
    
]
