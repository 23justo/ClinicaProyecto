from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegistroDoctor(models.Model):
    nombre = models.CharField(max_length = 60 , blank = False)
    email = models.EmailField()
    telefono = models.CharField(max_length = 8 , blank = True)
    direccion = models.CharField(max_length = 60 , blank = False)
    especialidad = models.CharField(max_length = 50 , blank = True)

    def __str__(self):
        return self.nombre

class Itinerario(models.Model):
    citas = models.CharField(max_length = 50, blank = False) # renombrar a hora
    paciente_itinerario = models.CharField(max_length = 50, blank = False) # renombrar a paciente
    doctor = models.CharField(max_length = 50, blank = False) #
    medicina = models.CharField(max_length = 50, blank = True)# renombre a fecha de cita
    cantidad_medicina = models.CharField(max_length = 200, blank = True) #renombre a Sintomas
    observacion = models.CharField(max_length = 200, blank = True) # renombrar a motivos

    def __str__(self):
        return self.citas

class Historial(models.Model):
    Historial_medico = models.CharField(max_length = 50, blank = False)
    citas_futuras = models.CharField(max_length = 50, blank = False)

    def __str__(self):
        return self.Historial_medico
