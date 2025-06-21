from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "nombre",
            "direccion",
            "mision",
            "vision",
            "anio_fundacion",
            "ruc",
            "imagen",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de la empresa"}
            ),
            "direccion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "mision": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "vision": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "anio_fundacion": forms.NumberInput(
                attrs={"class": "form-control", "min": 1900, "max": 2030}
            ),
            "ruc": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "RUC de la empresa"}
            ),
            "imagen": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
        labels = {
            "nombre": "Nombre de la Empresa",
            "direccion": "Dirección",
            "mision": "Misión",
            "vision": "Visión",
            "anio_fundacion": "Año de Fundación",
            "ruc": "RUC",
            "imagen": "Logo de la Empresa",
        }

    def clean_anio_fundacion(self):
        anio = self.cleaned_data.get("anio_fundacion")
        if anio and (anio < 1900 or anio > 2030):
            raise forms.ValidationError("El año debe estar entre 1900 y 2030")
        return anio
