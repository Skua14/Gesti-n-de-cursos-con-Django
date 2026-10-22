from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del curso")
    descripcion = models.TextField(verbose_name="Descripción del curso")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")

    def __str__(self):
        return self.nombre


# Create your models here.
