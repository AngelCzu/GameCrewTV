from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def inicio(request):
    salas =  Sala.objects.all()
    num_items = len(salas)

    salas_nombreSala = Sala.objects.filter(nombreSala = 2)
    return render(request, 'inicio.html', {"nomSala":salas, "nom_Sala":salas_nombreSala,"numitems":num_items})

def login_registro(request):
    context = {}  # Define el contexto vacío al principio.

    if request.method == 'POST':
        if 'txtUsuIng' in request.POST and 'txtPasswordIng' in request.POST:
            usuario = request.POST.get('txtUsuIng')
            clave = request.POST.get('txtPasswordIng')
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                # Usuario autenticado con éxito, puedes redirigirlo al inicio u otra página.
                return redirect('/inicio')
            else:
                # Usuario no válido, muestra un mensaje de error en el contexto.
                context['error'] = 'Credenciales inválidas. Intente nuevamente.'

        elif 'txtNomUsuReg' in request.POST and 'txtCorreoReg' in request.POST and 'txtPasswordReg' in request.POST:
            nombre_usuario = request.POST.get('txtNomUsuReg')
            correo = request.POST.get('txtCorreoReg')
            contraseña = request.POST.get('txtPasswordReg')

            # Crea un nuevo usuario
            user = User.objects.create_user(username=nombre_usuario, email=correo, password=contraseña)
            login(request, user)
            # Usuario registrado con éxito, puedes redirigirlo al inicio u otra página.
            return redirect('/inicio')
    # Renderiza la plantilla con el contexto, ya sea que el usuario se autentique o no.
    return render(request, 'login.html', context)

    

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



