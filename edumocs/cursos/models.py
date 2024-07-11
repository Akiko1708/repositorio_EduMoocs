from django.db import models
from django.utils import timezone
from datetime import datetime 
from django.contrib.auth.models import User


class Cursos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave de Curso")
    nombre = models.CharField(verbose_name="Nombre del Curso",max_length=50, default="")
    costo = models.DecimalField(verbose_name="Precio del Curso",max_digits=10, decimal_places=2, default=0.00)  
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio del Curso",default=timezone.now)
    fecha_termino = models.DateField(verbose_name="Fecha de Finalización del Curso",default=timezone.now)
    horas = models.IntegerField(verbose_name="Total de Horas del Curso",default=0)
    cupos = models.IntegerField(verbose_name="Limite de cupos",default=0)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    descripcion = models.TextField(verbose_name="Descripcion General del Curso",default="")
    profesor = models.CharField( max_length=50)
    created = models.DateTimeField(blank=True,default=datetime.now)
    updated = models.DateTimeField(blank=True,default=datetime.now)
    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")
        ordering = ["-created"]

    def _str_(self):
        return self.nombre
