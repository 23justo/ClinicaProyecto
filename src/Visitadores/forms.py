from django import forms
from .models import Registrar

class VisitadoresModelsForms(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = [
        "Nombre",
        "Apellido",
        "Telefono",
        "Email"
        ]
