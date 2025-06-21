from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    anio_fundacion = models.IntegerField()
    ruc = models.CharField(max_length=20, unique=True)
    imagen = models.ImageField(upload_to="empresa/", blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("empresa:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
