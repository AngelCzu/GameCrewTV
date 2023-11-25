from django import forms
from .models import *
class CompraSolespeForm(forms.Form):
    cantidad_solespe = forms.IntegerField(min_value=1, label='Cantidad de Solespe')
    numero_tarjeta = forms.CharField(max_length=16, label='Número de tarjeta')
    fecha_vencimiento = forms.CharField(max_length=5, label='Fecha de vencimiento (MM/YY)')
    codigo_seguridad = forms.CharField(max_length=3, label='Código de seguridad')
    correo_electronico = forms.CharField(max_length=100, label='correo electronico')