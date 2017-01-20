from django import forms

class FormularioRegistroDoctor(forms.Form):
    nombre = forms.CharField(max_length = 60)
    email = forms.EmailField()
    telefono = forms.CharField(max_length = 60)
    direccion = forms.CharField(max_length = 60)
    especialidad = forms.CharField(max_length = 60)

    def __str__(self):
        return self.nombre
