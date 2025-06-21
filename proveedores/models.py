from django.db import models
from django.urls import reverse


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("proveedores:list")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
