from django.contrib import admin
from .models import RegistroDoctor
from .models import Itinerario
from .models import Historial
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ['nombre','email','telefono','direccion','especialidad']
    class Meta:
        model = RegistroDoctor

class ItinerarioAdmin(admin.ModelAdmin):
    list_display = ['citas',
    'paciente',
    'doctor',
    'medicina',
    'cantidad_medicina']
    class Meta:
        model = Itinerario

class HistorialAdmin(admin.ModelAdmin):
    list_display = ['Historial_medico','citas_futuras']
    class Meta:
        model = Historial

admin.site.register(RegistroDoctor, AdminRegistrado)
admin.site.register(Itinerario, ItinerarioAdmin)
admin.site.register(Historial, HistorialAdmin)
