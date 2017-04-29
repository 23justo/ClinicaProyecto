from django import forms
from .models import RegistroDoctor,Itinerario,Historial

class FormularioRegistroDoctor(forms.ModelForm):
    class Meta:
        model = RegistroDoctor
        fields = [
        "nombre",
        "email",
        "telefono",
        "direccion",
        "especialidad",
        ]

class Formulario_para_itinerario(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = [
        "doctor",
        "paciente",
        "idMedicamento",
        "observacion",
        ]
