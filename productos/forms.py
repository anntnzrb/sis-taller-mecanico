from django import forms
from decimal import Decimal
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "iva", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del producto"}
            ),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01", "min": "0"}
            ),
            "iva": forms.Select(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
        labels = {
            "nombre": "Nombre del Producto",
            "descripcion": "Descripción",
            "precio": "Precio (USD)",
            "iva": "IVA",
            "imagen": "Imagen del Producto",
        }

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio and precio < Decimal("0"):
            raise forms.ValidationError("El precio no puede ser negativo")
        if precio and precio > Decimal("999999.99"):
            raise forms.ValidationError("El precio es demasiado alto")
        return precio
