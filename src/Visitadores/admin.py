from django.contrib import admin

from .models import Registrar

# Register your models here.
class visitadorRegistrado(admin.ModelAdmin):
    list_display = ["__str__", "Nombre"]


admin.site.register(Registrar, visitadorRegistrado)
