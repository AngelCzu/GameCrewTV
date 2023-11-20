from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.inicio), 
    path('login_registro', views.login_registro),
    path('inicio', views.inicio, name='inicio'),
    path('perfil', views.perfil),
    path('editar_perfil', views.editar_perfil), 
    path('streamStramer', views.streamStramer),
    path('formuSala', views.sala_form),
    path('streamViewer', views.streamViewer),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('comprar_solespe/', views.comprar_solespe, name='comprar_solespe'),
]
