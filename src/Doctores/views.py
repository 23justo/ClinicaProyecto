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
        form_data = formulario_para_doctor.cleaned_data

        nombre_limpio = form_data.get("nombre")
        email_limpio =form_data.get("email")
        telefono_limpio = form_data.get("telefono")
        direccion_limpio = form_data.get("direccion")
        especialidad_limpio = form_data.get("especialidad")

        objeto_doctor = RegistroDoctor.objects.create(nombre=nombre_limpio, email=email_limpio, telefono=telefono_limpio, direccion=direccion_limpio, especialidad=especialidad_limpio)


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
    Form_para_itinerario = Formulario_para_itinerario(request.POST or None)
    queryset = citas.objects.all()

    if Form_para_itinerario.is_valid():
        form_data = Form_para_itinerario.cleaned_data

        citas_limpio = form_data.get("citas")
        paciente_limpio =form_data.get("paciente_itinerario")
        doctor_limpio = form_data.get("doctor")
        medicina_limpio = form_data.get("medicina")
        cantidad_medicina_limpio = form_data.get("cantidad_medicina")
        observacion_limpio = form_data.get("observacion")

        objeto_itinerario = Itinerario.objects.create(citas=citas_limpio,paciente_itinerario=paciente_limpio,doctor=doctor_limpio,medicina=medicina_limpio, cantidad_medicina=cantidad_medicina_limpio,observacion=observacion_limpio)
    context = {
        "form": Form_para_itinerario,
        "queryset":queryset
    }
    return render(request, "Doctores/itinerario.html", context)
