from django.shortcuts import render
from .forms import FormularioRegistroDoctor
# Create your views here.
def paginadoctor(request):
    formulario_para_doctor= FormularioRegistroDoctor()
    context = {
        "form_doctor": formulario_para_doctor,
    }
    return render(request, "doctores.html", context)
