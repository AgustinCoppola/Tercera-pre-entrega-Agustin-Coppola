from django.db import models

# Create your models here.

class DjUser(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    email = models.CharField(max_length=30)

class Artist(models.Model):
    nombre = models.CharField(max_length=40)
    nombre_art = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(null=True)

class Track(models.Model):
    trackid = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField(null=True)