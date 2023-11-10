from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio), 
    path('login_registro',views.login_registro),  # ([Nombre Vista], views.[Nombre de la funcion en views.py])
    path('inicio', views.inicio),
    path('perfil', views.perfil, name='perfil'), 
    path('streamStramer', views.streamStramer),
    path('formuSala', views.sala_form),
    path('streamViewer', views.streamViewer),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil')

]
