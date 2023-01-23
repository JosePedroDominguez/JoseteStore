from django.db import models

# Create your models here.

OpcionesConsulta = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"],
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    tipoDeConsulta = models.IntegerField(choices=OpcionesConsulta) 
    mensaje = models.TextField()
    avisos = models.BooleanField()

def __str__(self):
    return self.nombre