from django.shortcuts import redirect, render
from .models import *


def inicio(request):
    salas =  Sala.objects.all()
    num_items = len(salas)

    salas_nombreSala = Sala.objects.filter(nombreSala = 2)
    return render(request, 'inicio.html', {"nomSala":salas, "nom_Sala":salas_nombreSala,"numitems":num_items})

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')
    
def streamStramer(request):
    return render(request, 'streamStramer.html')

def sala_form(request):
    nombre_sala = request.POST.get('txtSala')
    if nombre_sala:
        sala = Sala(nombreSala=nombre_sala)
        sala.save()
        return redirect('/streamStramer')
    return render(request, 'formuSala.html')


def streamViewer(request):
    return render(request, 'streamViewer.html')



