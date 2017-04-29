from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrar(models.Model):
    Nombre = models.CharField(max_length = 120, blank = True, null = False)
    Apellido = models.CharField(max_length = 120, blank = True, null = False)
    Telefono = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Nombre
