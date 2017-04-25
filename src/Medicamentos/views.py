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
