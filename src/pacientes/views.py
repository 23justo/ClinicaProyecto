from django.shortcuts import render
from django.shortcuts import redirect
from .forms import pacienteModelsForms,familiaModelsForms
from .models import paciente as modeloPaciente
from .models import familia as modeloFamilia
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy


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



def editar(request,id_paciente):
    paciente = modeloPaciente.objects.get(id=id_paciente)

    if request.method == 'GET':

        form = pacienteModelsForms(instance=paciente)
    else:
        form = pacienteModelsForms(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    return render(request,"pacientes/pacienteEditar.html",{'form':form})



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
