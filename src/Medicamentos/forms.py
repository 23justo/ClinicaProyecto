from django import forms
from .models import Registrar

class MedicamentosModelsForms(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = [
        "Nombre",
        
        "CasaMedica"
        ]
