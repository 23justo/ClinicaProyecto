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


    doctor = models.ForeignKey('Doctores.RegistroDoctor')
    paciente = models.ForeignKey('pacientes.paciente')
    idMedicamento = models.ForeignKey('Medicamentos.Registrar')
    observacion = models.CharField(max_length = 200, blank = True)
    fecha = models.DateField()

    def __str__(self):
        return self.observacion
