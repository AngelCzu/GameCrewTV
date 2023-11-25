from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio), 
    path('login_registro', views.login_registro, name='login_registro'),
    path('inicio', views.inicio, name='inicio'),
    path('perfil', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'), 
    path('streamStramer/<int:sala_id>/', views.streamStramer, name='streamStramer'),
    path('formuSala', views.sala_form, name='formuSala'),
    path('streamViewer/<int:sala_id>/', views.streamViewer, name='stream_viewer'),
    path('enviar_mensaje/<id>', views.enviar_mensaje, name='enviar_mensaje'),
    path('get_messages/<int:sala_id>/', views.get_messages, name='get_messages'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('comprar_solespe/', views.comprar_solespe, name='comprar_solespe'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
