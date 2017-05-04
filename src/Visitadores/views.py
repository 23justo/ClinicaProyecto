from django.shortcuts import render
from .forms import VisitadoresModelsForms
from .models import Registrar as re
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, ListView

def visitadores(request):
    # if request.method == "POST":
    #     print (request.POST)
    form = VisitadoresModelsForms(request.POST or None)
    queryset = re.objects.all()


    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = VisitadoresModelsForms()
        # print(instance)
        # print(instance.timestamp)


    context = {
    "form":form,
    "queryset":queryset,
    }
    return render(request,"Visitadores/visitadores.html",context)

def editar(request,id_visitador):
    visitador = re.objects.get(id=id_visitador)

    if request.method == 'GET':

        form = VisitadoresModelsForms(instance=visitador)
    else:
        form = VisitadoresModelsForms(request.POST, instance=visitador)
        if form.is_valid():
            form.save()
        return redirect('inicioUsu')
    return render(request,"Visitadores/visitadorEditar.html",{'form':form})
