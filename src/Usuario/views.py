from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def inicio(request):
    return render(request,"baseTemplate/inicio.html",{})

def inicioUsuario(request):
    return render(request,"baseTemplate/inicioUsuario.html",{})
