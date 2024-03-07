from django.db import models

class DirectorTecnico(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class AyudanteCampo(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class PreparadorFisico(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField() 

    def __str__(self):
        return self.nombre

class EntrenadorArqueros(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()       

    def __str__(self):
        return self.nombre

class Kinesiologo(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()    

    def __str__(self):
        return self.nombre