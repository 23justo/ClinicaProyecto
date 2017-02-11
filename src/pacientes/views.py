from django.shortcuts import render
from .forms import pacienteModelsForms

# Create your views here.
def inicio(request):
    return render(request,"index1.html",{})

def paciente(request):
    # if request.method == "POST":
    #     print (request.POST)
    form = pacienteModelsForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # print(instance)
        # print(instance.timestamp)


    context = {
    "form":form,
    }
    return render(request,"pacientes/creacionPaciente.html",context)
