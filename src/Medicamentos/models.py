from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrar(models.Model):
    Nombre = models.CharField(max_length = 120, blank = True, null = False)
    CasaMedica = models.CharField(max_length = 120, blank = True, null = False)
    Cantidad = models.IntegerField()


    def __unicode__(self):
        return self.Nombre
        
