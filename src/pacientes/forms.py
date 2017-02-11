from django import forms
from .models import paciente


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
