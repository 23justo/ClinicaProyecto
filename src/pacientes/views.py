from django.shortcuts import render
from .forms import pacienteModelsForms,familiaModelsForms

# Create your views here.
def inicio(request):
    return render(request,"baseTemplate/base.html",{})

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


def familia(request):
    form = familiaModelsForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
    "form":form
    }
    return render(request,"pacientes/creacionFamilias.html",context)
