from django import forms

class FormularioRegistroDoctor(forms.Form):
    nombre = forms.CharField(max_length = 60)
    email = forms.EmailField()
    telefono = forms.CharField(max_length = 60)
    direccion = forms.CharField(max_length = 60)
    especialidad = forms.CharField(max_length = 60)

    def __str__(self):
        return self.nombre

class Formulario_para_itinerario(forms.Form):
    citas = forms.CharField(max_length = 50)
    paciente_itinerario = forms.CharField(max_length = 50)
    doctor = forms.CharField(max_length = 50)
    medicina = forms.CharField(max_length = 50)
    cantidad_medicina = forms.CharField(max_length = 50)
    observacion = forms.CharField(max_length = 200)

    def __str__(self):
        return self.citas
