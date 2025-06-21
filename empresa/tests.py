from django.test import TestCase
from django.db import IntegrityError
from django.urls import reverse
from django.test import Client
from .models import Empresa
from .forms import EmpresaForm


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "nombre": "Taller Mecánico Los Expertos",
            "direccion": "Av. Principal 123, Ciudad",
            "mision": "Brindar servicios mecánicos de calidad",
            "vision": "Ser el taller mecánico líder en la región",
            "anio_fundacion": 2010,
            "ruc": "20123456789",
        }

    def test_create_empresa_with_valid_data(self):
        """Test creating a company with valid data"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertEqual(empresa.nombre, "Taller Mecánico Los Expertos")
        self.assertEqual(empresa.direccion, "Av. Principal 123, Ciudad")
        self.assertEqual(empresa.mision, "Brindar servicios mecánicos de calidad")
        self.assertEqual(empresa.vision, "Ser el taller mecánico líder en la región")
        self.assertEqual(empresa.anio_fundacion, 2010)
        self.assertEqual(empresa.ruc, "20123456789")

    def test_empresa_str_method(self):
        """Test string representation of company"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertEqual(str(empresa), "Taller Mecánico Los Expertos")

    def test_ruc_unique_constraint(self):
        """Test that RUC must be unique"""
        Empresa.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            Empresa.objects.create(
                nombre="Otro Taller",
                direccion="Otra dirección",
                mision="Otra misión",
                vision="Otra visión",
                anio_fundacion=2015,
                ruc="20123456789",  # Same RUC
            )

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        empresa = Empresa.objects.create(**self.valid_data)
        expected_url = reverse("empresa:nosotros")
        self.assertEqual(empresa.get_absolute_url(), expected_url)

    def test_imagen_field_optional(self):
        """Test that imagen field is optional"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertIsNone(empresa.imagen.name)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Empresa._meta.verbose_name, "Empresa")
        self.assertEqual(Empresa._meta.verbose_name_plural, "Empresas")

    def test_anio_fundacion_as_integer(self):
        """Test that anio_fundacion accepts integers"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertIsInstance(empresa.anio_fundacion, int)
        self.assertEqual(empresa.anio_fundacion, 2010)


class EmpresaFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "nombre": "Taller Mecánico Los Expertos",
            "direccion": "Av. Principal 123, Ciudad",
            "mision": "Brindar servicios mecánicos de calidad",
            "vision": "Ser el taller mecánico líder en la región",
            "anio_fundacion": 2010,
            "ruc": "20123456789",
        }

    def test_form_with_valid_data(self):
        """Test form validation with valid data"""
        form = EmpresaForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_form_save_creates_empresa(self):
        """Test that form.save() creates an Empresa instance"""
        form = EmpresaForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        empresa = form.save()
        self.assertIsInstance(empresa, Empresa)
        self.assertEqual(empresa.nombre, "Taller Mecánico Los Expertos")

    def test_form_required_fields(self):
        """Test that required fields show validation errors"""
        form = EmpresaForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)
        self.assertIn("direccion", form.errors)
        self.assertIn("mision", form.errors)
        self.assertIn("vision", form.errors)
        self.assertIn("anio_fundacion", form.errors)
        self.assertIn("ruc", form.errors)

    def test_anio_fundacion_validation(self):
        """Test anio_fundacion validation"""
        # Test valid year
        valid_data = self.valid_form_data.copy()
        valid_data["anio_fundacion"] = 2020
        form = EmpresaForm(data=valid_data)
        self.assertTrue(form.is_valid())

        # Test invalid year (too early)
        invalid_data = self.valid_form_data.copy()
        invalid_data["anio_fundacion"] = 1800
        form = EmpresaForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("anio_fundacion", form.errors)

        # Test invalid year (too late)
        invalid_data = self.valid_form_data.copy()
        invalid_data["anio_fundacion"] = 2050
        form = EmpresaForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("anio_fundacion", form.errors)

    def test_form_widgets_have_css_classes(self):
        """Test that form widgets have CSS classes"""
        form = EmpresaForm()
        self.assertIn("form-control", form.fields["nombre"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["direccion"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["mision"].widget.attrs["class"])

    def test_form_labels_in_spanish(self):
        """Test that form labels are in Spanish"""
        form = EmpresaForm()
        self.assertEqual(form.fields["nombre"].label, "Nombre de la Empresa")
        self.assertEqual(form.fields["direccion"].label, "Dirección")
        self.assertEqual(form.fields["mision"].label, "Misión")
        self.assertEqual(form.fields["vision"].label, "Visión")
        self.assertEqual(form.fields["anio_fundacion"].label, "Año de Fundación")
        self.assertEqual(form.fields["ruc"].label, "RUC")


class EmpresaViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.empresa_data = {
            "nombre": "Taller Mecánico Los Expertos",
            "direccion": "Av. Principal 123, Ciudad",
            "mision": "Brindar servicios mecánicos de calidad",
            "vision": "Ser el taller mecánico líder en la región",
            "anio_fundacion": 2010,
            "ruc": "20123456789",
        }

    def test_empresa_view_without_empresa(self):
        """Test empresa view when no empresa exists"""
        response = self.client.get(reverse("empresa:nosotros"))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["empresa"])

    def test_empresa_view_with_empresa(self):
        """Test empresa view when empresa exists"""
        empresa = Empresa.objects.create(**self.empresa_data)
        response = self.client.get(reverse("empresa:nosotros"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["empresa"], empresa)
