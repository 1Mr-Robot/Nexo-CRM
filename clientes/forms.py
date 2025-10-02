from django.forms import ModelForm
from django import forms
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'appaterno',
            'apmaterno',
            'fechanacimiento',
            'rfc',
            'curp',
            'generoid',
            'celular',
            'telefono',
            'correo',
            'codigopostal',
            'pais',
            'estado',
            'municipio',
            'ciudad',
            'colonia',
            'calle',
            'numcasa'
        ]
        widgets = {
            'fechanacimiento': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.fechanacimiento:
            self.fields['fechanacimiento'].initial = self.instance.fechanacimiento.strftime('%Y-%m-%d')