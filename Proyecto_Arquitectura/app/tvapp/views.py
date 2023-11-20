import time
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import threading

def agregar_puntos(usuario, cantidad):
    perfil, creado = Puntos.objects.get_or_create(usuario=usuario)
    perfil.puntos += cantidad
    perfil.save()

def agregar_puntos_periodicamente(usuario):
    while True:
        agregar_puntos(usuario, 10)
        time.sleep(60)



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
            agregar_puntos(user, 10)
            # Usuario registrado con éxito, puedes redirigirlo al inicio u otra página.
            return redirect('/inicio')
    # Renderiza la plantilla con el contexto, ya sea que el usuario se autentique o no.
    return render(request, 'login.html', context)

    
@login_required
def perfil(request):
    if request.method == 'POST' and 'logout' in request.POST:
        # Si se envía una solicitud POST con el nombre 'logout', entonces realiza el logout.
        logout(request)
        return redirect('inicio')  # Redirige al usuario a la página de inicio.

    usuario_actual = request.user
    username = usuario_actual.username
    email = usuario_actual.email
    puntos_usuario = Puntos.objects.get(usuario=request.user)
    return render(request, 'perfil.html', {'puntos_usuario': puntos_usuario})

@login_required
def editar_perfil(request):
    if request.method == 'POST' and 'logout' in request.POST:
        # Si se envía una solicitud POST con el nombre 'logout', entonces realiza el logout.
        logout(request)
        return redirect('inicio')  # Redirige al usuario a la página de inicio.

    usuario_actual = request.user
    username = usuario_actual.username
    email = usuario_actual.email
    return render(request, 'editar_perfil.html')
    
def streamStramer(request):
    return render(request, 'streamStramer.html')

def sala_form(request):
    nombre_sala = request.POST.get('txtSala')
    if nombre_sala:
        sala = Sala(nombreSala=nombre_sala)
        sala.save()
        return redirect('/streamStramer')
    return render(request, 'formuSala.html')

@login_required
def streamViewer(request):
    usuario_actual = request.user

    # Comenzar un hilo para agregar puntos en segundo plano
    puntos_thread = threading.Thread(target=agregar_puntos_periodicamente, args=(usuario_actual,))
    puntos_thread.daemon = True  # El hilo se detendrá cuando el programa principal se cierre
    puntos_thread.start()
    puntos_usuario = Puntos.objects.get(usuario=request.user)

    return render(request, 'streamViewer.html', {'puntos_usuario': puntos_usuario})

def comprar_solespe(request):
    if request.method == 'POST':
        form = CompraSolespeForm(request.POST)
        if form.is_valid():
            cantidad_solespe = form.cleaned_data['cantidad_solespe']
            numero_tarjeta = form.cleaned_data['numero_tarjeta']
            fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            codigo_seguridad = form.cleaned_data['codigo_seguridad']

            try:
                tarjeta = Tarjeta.objects.get(numeroTarjeta=numero_tarjeta, fechaVencimiento=fecha_vencimiento, codigoSeguridad=codigo_seguridad)
            except Tarjeta.DoesNotExist:
                messages.error(request, "La tarjeta no existe en la base de datos.")
                return redirect('comprar_solespe')

            costo_en_dinero = cantidad_solespe * 100  # 100 es el valor de cada Solespe

            if tarjeta.dinero < costo_en_dinero:
                messages.error(request, "Fondos insuficientes en la tarjeta.")
                return redirect('comprar_solespe')

            # Restar el costo de la compra al dinero de la tarjeta
            tarjeta.dinero -= costo_en_dinero
            tarjeta.save()

            # Puedes agregar puntos u otras acciones aquí
            agregar_puntos(request.user, cantidad_solespe)

            messages.success(request, f'Se han comprado {cantidad_solespe} Solespe con éxito.')
            return redirect('inicio')
    else:
        form = CompraSolespeForm()

    return render(request, 'comprar_solespe.html', {'form': form})


