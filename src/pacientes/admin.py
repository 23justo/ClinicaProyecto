from django.contrib import admin

from .models import paciente,familia
# Register your models here.
class pacienteAdmin(admin.ModelAdmin):
    list_display = [
    'nombre',
    'fechaNacimiento',
    'telefono',
    'genero',
    'edad',
    'tipoSangre',
    'dpi',
    'cui',
    'idFamilia',
    ]

class familiaAdmin(admin.ModelAdmin):
    list_display = [
    'primerApellido',
    'segundoApellido',
    ]

admin.site.register(paciente,pacienteAdmin)
admin.site.register(familia,familiaAdmin)
