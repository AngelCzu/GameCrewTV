from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages


# Create your models here.
class Sala(models.Model):
    nombreSala = models.CharField(max_length=100)  # Puedes ajustar la longitud máxima según tus necesidades

    def __str__(self):
        txt = "nombresala: {0}"
        return txt.format(self.nombreSala)

class Puntos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    
class Tarjeta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombreTitular = models.CharField(max_length=60)
    rut = models.CharField(max_length=9)
    numeroTarjeta = models.CharField(max_length=16)
    fechaVencimiento = models.CharField(max_length=4)
    codigoSeguridad = models.CharField(max_length=3)
    dinero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        txt = "Titular: {0}, RUT: {1}, Número de Tarjeta: {2}, Vencimiento: {3}, Código: {4}, Dinero: {5}"
        return txt.format(self.nombreTitular, self.rut, self.numeroTarjeta, self.fechaVencimiento, self.codigoSeguridad, self.dinero)


class Solespe(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cantidadSolespe = models.IntegerField(default=0)

    def __str__(self):
        txt = "Usuario: {0}, Solespe: {1}"
        return txt.format(self.usuario.username, self.cantidadSolespe)

class CompraSolespeForm(forms.Form):
    cantidad_solespe = forms.IntegerField(min_value=1, label='Cantidad de Solespe a comprar')
    numero_tarjeta = forms.CharField(max_length=16, label='Número de Tarjeta')
    fecha_vencimiento = forms.CharField(max_length=4, label='Fecha de Vencimiento (MMYY)')
    codigo_seguridad = forms.CharField(max_length=3, label='Código de Seguridad')

    def clean(self):
        cleaned_data = super().clean()
        # Validar la tarjeta en la base de datos
        numero_tarjeta = cleaned_data.get('numero_tarjeta')
        fecha_vencimiento = cleaned_data.get('fecha_vencimiento')
        codigo_seguridad = cleaned_data.get('codigo_seguridad')

        try:
            tarjeta = Tarjeta.objects.get(numeroTarjeta=numero_tarjeta, fechaVencimiento=fecha_vencimiento, codigoSeguridad=codigo_seguridad)
        except Tarjeta.DoesNotExist:
            raise forms.ValidationError("La tarjeta no existe en la base de datos.")

        # Restar el dinero de la tarjeta
        cantidad_solespe = cleaned_data.get('cantidad_solespe')
        costo_en_dinero = cantidad_solespe * 100  # 100 es el valor de cada Solespe

        if tarjeta.dinero < costo_en_dinero:
            raise forms.ValidationError("Fondos insuficientes en la tarjeta.")

        # Restar el costo de la compra al dinero de la tarjeta
        tarjeta.dinero -= costo_en_dinero
        tarjeta.save()

        # Actualizar la cantidad de Solespe del usuario
        usuario_solespe, creado = Solespe.objects.get_or_create(usuario=tarjeta.usuario)
        usuario_solespe.cantidadSolespe += cantidad_solespe
        usuario_solespe.save()

        return cleaned_data