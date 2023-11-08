from django.forms import ModelForm
from .models import *

class CreateHoja1(ModelForm):
    class Meta:
        model = Hoja1
        fields = ['nombre', 'apellido', 'dni', 'nacimiento', 'ingreso']

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']


class Hoja2Form(ModelForm):
    class Meta:
        model = Hoja2
        fields = ['calle', 'altura', 'localidad', 'correo', 'dni']

class CapacitacionForm(ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['nombre', 'Horas', 'puntaje', 'fecha', 'dni']