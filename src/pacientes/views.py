from django.shortcuts import render
from .forms import PacienteForm,RegForm

# Create your views here.
def inicio(request):
    return render(request,"index1.html",{})

def paciente(request):
    form = PacienteForm()
    context = {
    "form":form,
    }

    if form.is_valid():
        form.save()
    return render(request,"pacientes/creacionPaciente.html",context)
