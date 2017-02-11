from django.shortcuts import render
from .forms import pacienteModelsForms

# Create your views here.
def inicio(request):
    return render(request,"index1.html",{})

def paciente(request):
    form = pacienteModelsForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print("hola")
        print(instance)
        print(instance.timestamp)
        instance.save()

    context = {
    "form":form,
    }
    return render(request,"pacientes/creacionPaciente.html",context)
