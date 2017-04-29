from django.shortcuts import render
from .forms import MedicamentosModelsForms
from .models import Registrar as re

def medicamentos(request):
    # if request.method == "POST":
    #     print (request.POST)
    form = MedicamentosModelsForms(request.POST or None)
    queryset = re.objects.all()


    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = MedicamentosModelsForms()
        # print(instance)
        # print(instance.timestamp)


    context = {
    "form":form,
    "queryset":queryset,
    }
    return render(request,"Medicamentos/Medicamentos.html",context)


def editar(request,id_medicamento):
    medicamento = re.objects.get(id=id_medicamento)

    if request.method == 'GET':

        form = MedicamentosModelsForms(instance=medicamento)
    else:
        form = pacienteModelsForms(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
        return redirect('inicio')
    return render(request,"Medicamentos/medicamentoEditar.html",{'form':form})
