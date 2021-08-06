from django.db import models

# Create your models here.
class Escritor(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre=models.CharField(max_length=50)
    editorial=models.CharField(max_length=50)
    codigo=models.CharField(max_length=10)
    escritor=models.ForeignKey(Escritor,on_delete=models.CASCADE)