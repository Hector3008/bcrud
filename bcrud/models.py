from django.db import models


# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=40)
    rate=models.BigIntegerField()
    descripcion=models.CharField(max_length=4000)

class Entrada(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=200)
    texto=models.CharField(max_length=20000)

class Comentario(models.Model):
    Comentador=models.CharField(max_length=100)
    Texto=models.CharField(max_length=500)
    Like=models.BooleanField()

class Categoria(models.Model):
    nombres=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    fecha=models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)
