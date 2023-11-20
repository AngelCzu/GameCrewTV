from django import forms

class CompraSolespeForm(forms.Form):
    cantidad_solespe = forms.IntegerField(min_value=1, label='Cantidad de Solespe')
    tarjeta_credito = forms.ModelChoiceField(queryset=Tarjeta.objects.all(), label='Seleccionar Tarjeta')

