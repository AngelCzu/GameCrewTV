from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio), 
    path('login',views.login),  # ([Nombre Vista], views.[Nombre de la funcion en views.py])
    path('inicio', views.inicio),
    path('perfil', views.perfil), 
    path('streamStramer', views.streamStramer),
    path('formuSala', views.sala_form),
    path('streamViewer', views.streamViewer)

]
