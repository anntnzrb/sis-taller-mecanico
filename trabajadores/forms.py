from django import forms
from .models import Trabajador


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ["nombre", "apellido", "correo", "cedula", "codigo_empleado", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese el nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ingrese el apellido"}
            ),
            "correo": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "correo@ejemplo.com"}
            ),
            "cedula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Número de cédula"}
            ),
            "codigo_empleado": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Código de empleado"}
            ),
            "imagen": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "correo": "Correo Electrónico",
            "cedula": "Cédula",
            "codigo_empleado": "Código de Empleado",
            "imagen": "Fotografía",
        }

    def clean_correo(self):
        correo = self.cleaned_data.get("correo")
        if correo and "@" not in correo:
            raise forms.ValidationError("Ingrese un correo electrónico válido")
        return correo

    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if cedula and len(cedula) < 8:
            raise forms.ValidationError("La cédula debe tener al menos 8 caracteres")
        return cedula

    def clean_codigo_empleado(self):
        codigo = self.cleaned_data.get("codigo_empleado")
        if codigo and len(codigo) < 3:
            raise forms.ValidationError(
                "El código de empleado debe tener al menos 3 caracteres"
            )
        return codigo
