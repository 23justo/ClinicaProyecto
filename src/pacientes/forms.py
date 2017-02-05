from django import forms
from .models import paciente

class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length = 45)
    fechaNacimiento = forms.DateField()
    telefono = forms.CharField(max_length = 8)
    genero = forms.CharField(max_length = 9)
    edad = forms.IntegerField()
    tipoSangre = forms.CharField(max_length = 3)
    dpi = forms.CharField(max_length = 40)
    cui = forms.CharField(max_length = 40)
    # idFamilia = forms.ModelChoiceField()

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
