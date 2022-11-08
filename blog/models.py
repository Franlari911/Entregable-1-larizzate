

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AutosNuevo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    fecha_de_fabricacion = models.DateField(null=True)
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return self.marca + self.modelo
    


class AutosUsado(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_de_fabricacion = models.DateField(null=True)
    fecha_de_patentacion = models.DateField(null=True)
    def __str__(self):
        return self.marca + self.modelo


class MotosNueva(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    cilindrada = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_de_fabricacion = models.DateField(null=True)
    def __str__(self):
        return self.marca + self.modelo


class MotosUsada(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    cilindrada = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_de_fabricacion = models.DateField(null=True)
    fecha_de_patentacion = models.DateField(null=True)
    def __str__(self):
        return self.marca + self.modelo



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
