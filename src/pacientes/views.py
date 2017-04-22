from django.shortcuts import render
from .forms import pacienteModelsForms,familiaModelsForms
from .models import paciente as modeloPaciente
from .models import familia as modeloFamilia

# Create your views here.
def inicio(request):
    return render(request,"baseTemplate/inicio.html",{})

def paciente(request):
    # if request.method == "POST":
    #     print (request.POST)
    form = pacienteModelsForms(request.POST or None)
    queryset = modeloPaciente.objects.all()


    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = pacienteModelsForms()
        # print(instance)
        # print(instance.timestamp)


    context = {
    "form":form,
    "queryset":queryset,
    }
    return render(request,"pacientes/creacionPaciente.html",context)


def familia(request):
    form = familiaModelsForms(request.POST or None)
    queryset = modeloFamilia.objects.all()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        fromm = familiaModelsForms()

    context = {
    "form":form,
    "queryset":queryset,
    }
    return render(request,"pacientes/creacionFamilias.html",context)
