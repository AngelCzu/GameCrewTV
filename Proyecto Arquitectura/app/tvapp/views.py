from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def vista2(request):
    return render(request, 'vistaDos.html')
