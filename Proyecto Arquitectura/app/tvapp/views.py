from django.shortcuts import redirect, render
from .models import *


def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')
    
def stream(request):
    return render(request, 'stream.html')

def sala_form(request):
    nombre_sala = request.POST.get('txtSala')
    if nombre_sala:
        sala = Sala(nombreSala=nombre_sala)
        sala.save()
    return render(request, 'formuSala.html')
