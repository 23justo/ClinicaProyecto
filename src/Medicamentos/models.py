from django.db import models

# Create your models here.
class Registrar(models.Model):
    Nombre = models.CharField(max_length = 120, blank = True, null = False)
    CasaMedica = models.CharField(max_length = 120, blank = True, null = False)
    Visitador_id = models.ForeignKey('Visitadores.Registrar');


    def __str__(self):
        return self.Nombre
