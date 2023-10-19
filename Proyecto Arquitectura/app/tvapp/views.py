from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')
    
def stream(request):
    return render(request, 'stream.html')
