from django.test import TestCase
from django.urls import reverse
from .models import Proveedor
from .forms import ProveedorForm


class ProveedorModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "nombre": "Repuestos Automotrices SA",
            "descripcion": "Proveedor especializado en repuestos y accesorios automotrices",
            "telefono": "+593-2-2345678",
            "pais": "Ecuador",
            "correo": "ventas@repuestossa.com",
            "direccion": "Av. América 456, Quito",
        }

    def test_create_proveedor_with_valid_data(self):
        """Test creating a supplier with valid data"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertEqual(proveedor.nombre, "Repuestos Automotrices SA")
        self.assertEqual(
            proveedor.descripcion,
            "Proveedor especializado en repuestos y accesorios automotrices",
        )
        self.assertEqual(proveedor.telefono, "+593-2-2345678")
        self.assertEqual(proveedor.pais, "Ecuador")
        self.assertEqual(proveedor.correo, "ventas@repuestossa.com")
        self.assertEqual(proveedor.direccion, "Av. América 456, Quito")

    def test_proveedor_str_method(self):
        """Test string representation of supplier"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertEqual(str(proveedor), "Repuestos Automotrices SA")

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        expected_url = reverse("proveedores:list")
        self.assertEqual(proveedor.get_absolute_url(), expected_url)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Proveedor._meta.verbose_name, "Proveedor")
        self.assertEqual(Proveedor._meta.verbose_name_plural, "Proveedores")

    def test_correo_field_validation(self):
        """Test that correo field accepts valid email"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertTrue("@" in proveedor.correo)
        self.assertTrue("." in proveedor.correo)

    def test_all_fields_required(self):
        """Test that all fields are properly set"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertIsNotNone(proveedor.nombre)
        self.assertIsNotNone(proveedor.descripcion)
        self.assertIsNotNone(proveedor.telefono)
        self.assertIsNotNone(proveedor.pais)
        self.assertIsNotNone(proveedor.correo)
        self.assertIsNotNone(proveedor.direccion)

    def test_text_fields_accept_long_content(self):
        """Test that text fields accept longer content"""
        long_description = "A" * 500
        long_address = "B" * 300

        data = self.valid_data.copy()
        data["descripcion"] = long_description
        data["direccion"] = long_address

        proveedor = Proveedor.objects.create(**data)
        self.assertEqual(proveedor.descripcion, long_description)
        self.assertEqual(proveedor.direccion, long_address)


class ProveedorFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "nombre": "Repuestos Automotrices SA",
            "descripcion": "Proveedor especializado en repuestos y accesorios automotrices",
            "telefono": "+593-2-2345678",
            "pais": "Ecuador",
            "correo": "ventas@repuestossa.com",
            "direccion": "Av. América 456, Quito",
        }

    def test_form_with_valid_data(self):
        """Test form validation with valid data"""
        form = ProveedorForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_form_save_creates_proveedor(self):
        """Test that form.save() creates a Proveedor instance"""
        form = ProveedorForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        proveedor = form.save()
        self.assertIsInstance(proveedor, Proveedor)
        self.assertEqual(proveedor.nombre, "Repuestos Automotrices SA")

    def test_form_required_fields(self):
        """Test that required fields show validation errors"""
        form = ProveedorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)
        self.assertIn("descripcion", form.errors)
        self.assertIn("telefono", form.errors)
        self.assertIn("pais", form.errors)
        self.assertIn("correo", form.errors)
        self.assertIn("direccion", form.errors)

    def test_telefono_validation_too_short(self):
        """Test telefono validation for short numbers"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["telefono"] = "123"
        form = ProveedorForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("telefono", form.errors)
        self.assertIn("al menos 7 dígitos", str(form.errors["telefono"]))

    def test_telefono_validation_valid_length(self):
        """Test telefono validation for valid length"""
        valid_data = self.valid_form_data.copy()
        valid_data["telefono"] = "1234567"
        form = ProveedorForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_correo_validation(self):
        """Test email field validation"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["correo"] = "invalid-email"
        form = ProveedorForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("correo", form.errors)

    def test_form_widgets_have_css_classes(self):
        """Test that form widgets have CSS classes"""
        form = ProveedorForm()
        self.assertIn("form-control", form.fields["nombre"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["descripcion"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["telefono"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["correo"].widget.attrs["class"])

    def test_form_labels_in_spanish(self):
        """Test that form labels are in Spanish"""
        form = ProveedorForm()
        self.assertEqual(form.fields["nombre"].label, "Nombre del Proveedor")
        self.assertEqual(form.fields["descripcion"].label, "Descripción")
        self.assertEqual(form.fields["telefono"].label, "Teléfono")
        self.assertEqual(form.fields["pais"].label, "País")
        self.assertEqual(form.fields["correo"].label, "Correo Electrónico")
        self.assertEqual(form.fields["direccion"].label, "Dirección")

    def test_form_placeholders(self):
        """Test that form widgets have appropriate placeholders"""
        form = ProveedorForm()
        self.assertEqual(
            form.fields["nombre"].widget.attrs["placeholder"], "Nombre del proveedor"
        )
        self.assertEqual(
            form.fields["telefono"].widget.attrs["placeholder"], "+593-99-999-9999"
        )
        self.assertEqual(
            form.fields["correo"].widget.attrs["placeholder"], "correo@proveedor.com"
        )
