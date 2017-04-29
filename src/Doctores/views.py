from django.shortcuts import render
from .forms import FormularioRegistroDoctor, Formulario_para_itinerario
from .models import RegistroDoctor, Itinerario
from .models import RegistroDoctor as modeloDoctor
from .models import Itinerario as citas
# Create your views here.
def inicio(request):
    return render(request,"baseTemplate/inicio.html",{})

def paginadoctor(request):
    formulario_para_doctor= FormularioRegistroDoctor(request.POST or None)
    queryset = modeloDoctor.objects.all()

    if formulario_para_doctor.is_valid():
        instance = formulario_para_doctor(commit=False)
        insatnce.save()
        formulario_para_doctor = formulario_para_doctor()




    context = {
        "form": formulario_para_doctor,
        "queryset":queryset
    }
    return render(request, "Doctores/doctores.html", context)


def editar(request,id_doctor):
    doctor = modeloDoctor.objects.get(id=id_doctor)

    if request.method == 'GET':

        form = FormularioRegistroDoctor(instance=doctor)
    else:
        form = FormularioRegistroDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    return render(request,"Doctores/doctorEditar.html",{'form':form})

def paginaitinerario(request):
    form = Formulario_para_itinerario(request.POST or None)
    queryset = citas.objects.all()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = Formulario_para_itinerario()

    context = {
        "form": form,
        "queryset":queryset
    }
    return render(request, "Doctores/itinerario.html", context)


def editarCita(request,id_cita):
    cita = citas.objects.get(id=id_cita)

    if request.method == 'GET':

        form = Formulario_para_itinerario(instance=cita)
    else:
        form = Formulario_para_itinerario(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    return render(request,"Doctores/citaEditar.html",{'form':form})
