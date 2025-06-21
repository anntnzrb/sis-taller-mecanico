from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "descripcion", "telefono", "pais", "correo", "direccion"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del proveedor"}
            ),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+593-99-999-9999"}
            ),
            "pais": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "País"}
            ),
            "correo": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "correo@proveedor.com"}
            ),
            "direccion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "nombre": "Nombre del Proveedor",
            "descripcion": "Descripción",
            "telefono": "Teléfono",
            "pais": "País",
            "correo": "Correo Electrónico",
            "direccion": "Dirección",
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if telefono and len(telefono) < 7:
            raise forms.ValidationError("El teléfono debe tener al menos 7 dígitos")
        return telefono
