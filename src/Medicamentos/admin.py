from django.contrib import admin

from .models import Registrar

# Register your models here.
class MedicamentoRegistrar(admin.ModelAdmin):
    list_display = ["Nombre","CasaMedica","Visitador_id"]
    class Meta:
        mmodel = Registrar

admin.site.register(Registrar, MedicamentoRegistrar)
