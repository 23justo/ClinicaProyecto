from django.contrib import admin

from .models import paciente,familia
from .forms import pacienteModelsForms
# Register your models here.
class pacienteAdmin(admin.ModelAdmin):
    list_display = [
    'nombre',
    'fechaNacimiento',
    'telefono',
    'genero',
    'tipoSangre',
    'dpi',
    'cui',
    'idFamilia',
    ]
    form = pacienteModelsForms

class familiaAdmin(admin.ModelAdmin):
    list_display = [
    'primerApellido',
    'segundoApellido',
    ]

admin.site.register(paciente,pacienteAdmin)
admin.site.register(familia,familiaAdmin)
