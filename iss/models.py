from django.db import models
from django.utils import timezone
from django.shortcuts import render
# Create your models here.

class Cartas(models.Model):
    idbiblioteca = models.IntegerField(primary_key=True, verbose_name="IDBIBLIOTECA")
    juego = models.TextField(max_length=50, default="Juego", verbose_name="JUEGO")
    sets = models.TextField(max_length=50, default="Sets", verbose_name="SETS")
    idcarta = models.IntegerField(default = 0, verbose_name="IDCARTA")
    nombrecarta = models.TextField(max_length=50, default="Nombre Carta", verbose_name="NOMBRECARTA")    
    habilidad = models.TextField(max_length=250, default="Habilidad", verbose_name="HABILIDAD")
    keyword = models.TextField(max_length=50, default="Keyword", verbose_name="KEYWORD")    
    costomana = models.IntegerField(default = 0, verbose_name="COSTOMANA")
    fuerza = models.IntegerField( default = 0, verbose_name="FUERZA")    
    salud = models.IntegerField(default = 0, verbose_name="SALUD")
    rareza = models.TextField(max_length=50, default="Rareza", verbose_name="RAREZA")    
    tipocarta = models.TextField(max_length=50, default="Tipo carta", verbose_name="TIPOCARTA")
    region = models.TextField(max_length=50, default="Region", verbose_name="REGION")
    tipohechizo = models.TextField(max_length=50, default="Tipo hechizo", verbose_name="TIPOHECHIZO")
    class Meta:
        db_table='home_cartas'

class Observaciones(models.Model):
    idobservacion = models.IntegerField(primary_key=True, verbose_name="IDOBSERVACION")
    nombrejugador = models.TextField(max_length=50, default="Juego", verbose_name="NOMBREJUGADOR")
    fecha_creacion = models.DateTimeField(default=timezone.now)
    actividad = models.TextField(default = 0, verbose_name="ACTIVIDAD")
    observacion = models.TextField(max_length=50, default="Nombre Carta", verbose_name="OBSERVACION")  
    class Meta:
        db_table='home_observaciones'

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    clave = models.CharField(max_length=50, default='')
    class Meta:
        db_table = 'home_usuarios'
    def __str__(self):
        return self.nombre
    def __unicode__(self):
        return self.nombre