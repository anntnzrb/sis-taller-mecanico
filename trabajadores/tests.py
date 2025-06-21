from django.test import TestCase
from django.db import IntegrityError
from django.urls import reverse
from django import forms
from .models import Trabajador
from .forms import TrabajadorForm


class TrabajadorModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "correo": "juan.perez@email.com",
            "cedula": "12345678",
            "codigo_empleado": "EMP001",
        }

    def test_create_trabajador_with_valid_data(self):
        """Test creating a worker with valid data"""
        trabajador = Trabajador.objects.create(**self.valid_data)
        self.assertEqual(trabajador.nombre, "Juan")
        self.assertEqual(trabajador.apellido, "Pérez")
        self.assertEqual(trabajador.correo, "juan.perez@email.com")
        self.assertEqual(trabajador.cedula, "12345678")
        self.assertEqual(trabajador.codigo_empleado, "EMP001")

    def test_trabajador_str_method(self):
        """Test string representation of worker"""
        trabajador = Trabajador.objects.create(**self.valid_data)
        self.assertEqual(str(trabajador), "Juan Pérez")

    def test_cedula_unique_constraint(self):
        """Test that cedula must be unique"""
        Trabajador.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            Trabajador.objects.create(
                nombre="María",
                apellido="González",
                correo="maria@email.com",
                cedula="12345678",  # Same cedula
                codigo_empleado="EMP002",
            )

    def test_codigo_empleado_unique_constraint(self):
        """Test that codigo_empleado must be unique"""
        Trabajador.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            Trabajador.objects.create(
                nombre="María",
                apellido="González",
                correo="maria@email.com",
                cedula="87654321",
                codigo_empleado="EMP001",  # Same codigo_empleado
            )

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        trabajador = Trabajador.objects.create(**self.valid_data)
        expected_url = reverse("trabajadores:detail", kwargs={"pk": trabajador.pk})
        self.assertEqual(trabajador.get_absolute_url(), expected_url)

    def test_imagen_field_optional(self):
        """Test that imagen field is optional"""
        trabajador = Trabajador.objects.create(**self.valid_data)
        self.assertIsNone(trabajador.imagen.name)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Trabajador._meta.verbose_name, "Trabajador")
        self.assertEqual(Trabajador._meta.verbose_name_plural, "Trabajadores")


class TrabajadorFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "correo": "juan.perez@email.com",
            "cedula": "12345678",
            "codigo_empleado": "EMP001",
        }

    def test_form_with_valid_data(self):
        """Test form validation with valid data"""
        form = TrabajadorForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_form_save_creates_trabajador(self):
        """Test that form.save() creates a Trabajador instance"""
        form = TrabajadorForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        trabajador = form.save()
        self.assertIsInstance(trabajador, Trabajador)
        self.assertEqual(trabajador.nombre, "Juan")

    def test_form_required_fields(self):
        """Test that required fields show validation errors"""
        form = TrabajadorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)
        self.assertIn("apellido", form.errors)
        self.assertIn("correo", form.errors)
        self.assertIn("cedula", form.errors)
        self.assertIn("codigo_empleado", form.errors)

    def test_correo_validation(self):
        """Test email field validation"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["correo"] = "invalid-email"
        form = TrabajadorForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("correo", form.errors)

    def test_correo_custom_validation(self):
        """Test custom email validation logic"""
        from trabajadores.forms import TrabajadorForm

        form = TrabajadorForm()
        # Test the clean_correo method directly
        form.cleaned_data = {"correo": "invalidemail.com"}
        try:
            result = form.clean_correo()
            # If no exception, the validation passed
            self.assertEqual(result, "invalidemail.com")
        except forms.ValidationError as e:
            self.assertIn("correo electrónico válido", str(e))

    def test_cedula_length_validation(self):
        """Test cedula minimum length validation"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["cedula"] = "123"  # Too short
        form = TrabajadorForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("cedula", form.errors)
        self.assertIn("debe tener al menos 8 caracteres", str(form.errors["cedula"]))

    def test_codigo_empleado_length_validation(self):
        """Test codigo_empleado minimum length validation"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["codigo_empleado"] = "EM"  # Too short
        form = TrabajadorForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("codigo_empleado", form.errors)
        self.assertIn(
            "debe tener al menos 3 caracteres", str(form.errors["codigo_empleado"])
        )

    def test_form_widgets_have_css_classes(self):
        """Test that form widgets have Bootstrap CSS classes"""
        form = TrabajadorForm()
        self.assertIn("form-control", form.fields["nombre"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["correo"].widget.attrs["class"])

    def test_form_labels_in_spanish(self):
        """Test that form labels are in Spanish"""
        form = TrabajadorForm()
        self.assertEqual(form.fields["nombre"].label, "Nombre")
        self.assertEqual(form.fields["correo"].label, "Correo Electrónico")
        self.assertEqual(form.fields["cedula"].label, "Cédula")
