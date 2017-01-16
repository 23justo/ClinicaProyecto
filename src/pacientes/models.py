from django.db import models

# Create your models here.
class paciente(models.Model):
    nombre = models.CharField(max_length = 45, blank = False)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length = 8 , blank = True)
    genero = models.CharField(max_length = 9 ,blank = False)
    edad = models.IntegerField()
    tipoSangre = models.CharField(max_length = 3)
    dpi = models.CharField(max_length = 30 , blank = False)
    cui = models.CharField(max_length = 30 , blank = False)
    idFamilia = models.ForeignKey('familia')

    def __str__(self):
        return self.nombre

class familia(models.Model):
    primerApellido = models.CharField(max_length = 45 , blank = False)
    segundoApellido = models.CharField(max_length = 45 , blank = False)

    def __str__(self):
        return self.primerApellido + self.segundoApellido
