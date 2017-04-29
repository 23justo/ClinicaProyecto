from django.contrib import admin
from .models import RegistroDoctor
from .models import Itinerario

# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ['nombre','email','telefono','direccion','especialidad']
    class Meta:
        model = RegistroDoctor

class ItinerarioAdmin(admin.ModelAdmin):
    list_display = [

    'doctor',
    'paciente',
    'idMedicamento',
    'observacion',
    'fecha'
    ]
    class Meta:
        model = Itinerario



admin.site.register(RegistroDoctor, AdminRegistrado)
admin.site.register(Itinerario, ItinerarioAdmin)
