from django.db import models
from django.urls import reverse


class Producto(models.Model):
    IVA_CHOICES = [
        (0, "0%"),
        (15, "15%"),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.IntegerField(choices=IVA_CHOICES, default=15)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("productos:detail", kwargs={"pk": self.pk})

    @property
    def precio_con_iva(self):
        return self.precio * (1 + self.iva / 100)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
