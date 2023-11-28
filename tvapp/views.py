from datetime import timezone
import time
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 
from .forms import CompraSolespeForm
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
            agregar_puntos(user, 50)
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
    solespe_usuario, creado = Solespe.objects.get_or_create(usuario=request.user)
    return render(request, 'perfil.html', {'puntos_usuario': puntos_usuario, 'solespe_usuario': solespe_usuario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Actualiza los datos del usuario
        user = request.user
        user.username = username
        user.email = email
        user.save()

        # Redirige de vuelta al perfil
        return redirect('perfil')

    return render(request, 'editar_perfil.html')

@login_required    
def streamStramer(request, sala_id):
    usuario_actual = request.user
    puntos_usuario = None

    sala = get_object_or_404(Sala, id=sala_id)
    mensajes = MensajeChat.objects.filter(sala=sala).order_by('timestamp')

    if usuario_actual.is_authenticated:
        puntos_usuario, created = Puntos.objects.get_or_create(usuario=request.user)
        
        if request.method == 'GET':
            sala = get_object_or_404(Sala, id=sala_id)
            mensajes = MensajeChat.objects.filter(sala=sala).order_by('timestamp')

            data = [{'usuario': mensaje.usuario.username, 'mensaje': mensaje.mensaje, 'timestamp': str(mensaje.timestamp)} for mensaje in mensajes]
    return render(request, 'streamStramer.html', { 'sala': sala, 'mensajes': mensajes, 'puntos_usuario': puntos_usuario})

def sala_form(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        v_categoria_id = request.POST.get('cmbCategoria')
        v_categoria = Categoria.objects.get(id_categoria=v_categoria_id)
        nombre_sala = request.POST.get('txtSala')
        
        if nombre_sala:
            sala = Sala(nombreSala=nombre_sala, categoriaId=v_categoria)
            sala.save()
            sala_id = sala.id
            return redirect(f'/streamStramer/{sala_id}/')
    
    return render(request, 'formuSala.html', {"cate": categorias})


def streamViewer(request, sala_id):
    usuario_actual = request.user
    puntos_usuario = None

    sala = get_object_or_404(Sala, id=sala_id)
    mensajes = MensajeChat.objects.filter(sala=sala).order_by('timestamp')

    if usuario_actual.is_authenticated:
        puntos_usuario, created = Puntos.objects.get_or_create(usuario=request.user)
        
        if request.method == 'GET':
            sala = get_object_or_404(Sala, id=sala_id)
            mensajes = MensajeChat.objects.filter(sala=sala).order_by('timestamp')

            data = [{'usuario': mensaje.usuario.username, 'mensaje': mensaje.mensaje, 'timestamp': str(mensaje.timestamp)} for mensaje in mensajes]
        
           

    return render(request, 'streamViewer.html', { 'sala': sala, 'mensajes': mensajes, 'puntos_usuario': puntos_usuario})

from django.http import JsonResponse

def enviar_mensaje(request, id):
    try:
        v_mensaje = request.POST.get('mensaje', '')
        destacar = request.POST.get('destacar', False)
        sticker = request.POST.get('sticker', None)
        usuario = request.user

        if id and v_mensaje:
            sala = get_object_or_404(Sala, id=id)
            mensaje = MensajeChat.objects.create(
                usuario=usuario,
                sala=sala,
                mensaje=v_mensaje,
                destacado=destacar,
                sticker=sticker
            )

            return JsonResponse({
                'status': 'OK',
                'mensaje': {
                    'usuario': mensaje.usuario.username,
                    'mensaje': mensaje.mensaje,
                    'timestamp': str(mensaje.timestamp),
                    'destacado': mensaje.destacado,
                    'sticker': mensaje.sticker,
                }
            })
        else:
            return JsonResponse({'status': 'ERROR', 'message': 'Datos insuficientes'})

    except Exception as e:
        return JsonResponse({'status': 'ERROR', 'message': str(e)})

    

def get_messages(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    mensajes = MensajeChat.objects.filter(sala=sala).order_by('timestamp')
    
    data = [{'usuario': mensaje.usuario.username, 'mensaje': mensaje.mensaje, 'timestamp': str(mensaje.timestamp)} for mensaje in mensajes]
    
    return JsonResponse({'mensajes': data})


def agregar_solespe(usuario, cantidad_solespe):
    # Obtener o crear el objeto Solespe asociado al usuario
    usuario_solespe, creado = Solespe.objects.get_or_create(usuario=usuario)
    usuario_solespe.cantidadSolespe += cantidad_solespe
    usuario_solespe.save()

def comprar_solespe(request):
    if request.method == 'POST':
        form = CompraSolespeForm(request.POST)
        if form.is_valid():
            cantidad_solespe = form.cleaned_data['cantidad_solespe']
            numero_tarjeta = form.cleaned_data['numero_tarjeta']
            fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            codigo_seguridad = form.cleaned_data['codigo_seguridad']
            correo_electronico = form.cleaned_data['correo_electronico']  # Nuevo campo de correo electrónico

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

            # Agregar Solespe al usuario
            agregar_solespe(request.user, cantidad_solespe)


            # Enviar correo electrónico
            subject = 'Compra exitosa de Solespe'
            #mensaje = f'Gracias por tu compra en Solespe. Se han comprado {cantidad_solespe} Solespe con éxito.'
            
            to_email = correo_electronico

            subject = 'Compra exitosa de Solespe' #Welcome to DataFlair'
            message = f'Gracias por tu compra en Solespe. Se han comprado {cantidad_solespe} Solespe con éxito.' #'Hope you are enjoying your Django Tutorials'
            recepient = to_email
            send_mail(subject, message, 
            settings.EMAIL_HOST_USER, 
            [recepient], 
            fail_silently = False)
            return redirect('inicio')
    else:
        form = CompraSolespeForm()

    return render(request, 'comprar_solespe.html', {'form': form})