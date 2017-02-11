from django import forms
from .models import paciente,familia


class pacienteModelsForms(forms.ModelForm):
    class Meta:
        model = paciente
        fields = [
        "nombre",
        "fechaNacimiento",
        "telefono",
        "genero",
        "tipoSangre",
        "dpi",
        "cui",
        "idFamilia",
            ]

class familiaModelsForms(forms.ModelForm):
    class Meta:
        model = familia
        fields = [
        "primerApellido",
        "segundoApellido",
            ]
