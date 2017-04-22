from django.contrib import admin

from .models import Registrar

# Register your models here.
class visitadorRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "Nombre"]
    class Meta:
        model = Registrar

admin.site.register(Registrar, visitadorRegistrado)
