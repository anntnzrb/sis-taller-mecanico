from django.db import models
from django.urls import reverse


class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    cedula = models.CharField(max_length=20, unique=True)
    codigo_empleado = models.CharField(max_length=20, unique=True)
    imagen = models.ImageField(upload_to="trabajadores/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_absolute_url(self):
        return reverse("trabajadores:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
