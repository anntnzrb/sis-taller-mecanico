from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.urls import reverse
from .models import Empresa


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'nombre': 'Taller Mecánico Los Expertos',
            'direccion': 'Av. Principal 123, Ciudad',
            'mision': 'Brindar servicios mecánicos de calidad',
            'vision': 'Ser el taller mecánico líder en la región',
            'anio_fundacion': 2010,
            'ruc': '20123456789'
        }

    def test_create_empresa_with_valid_data(self):
        """Test creating a company with valid data"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertEqual(empresa.nombre, 'Taller Mecánico Los Expertos')
        self.assertEqual(empresa.direccion, 'Av. Principal 123, Ciudad')
        self.assertEqual(empresa.mision, 'Brindar servicios mecánicos de calidad')
        self.assertEqual(empresa.vision, 'Ser el taller mecánico líder en la región')
        self.assertEqual(empresa.anio_fundacion, 2010)
        self.assertEqual(empresa.ruc, '20123456789')

    def test_empresa_str_method(self):
        """Test string representation of company"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertEqual(str(empresa), 'Taller Mecánico Los Expertos')

    def test_ruc_unique_constraint(self):
        """Test that RUC must be unique"""
        Empresa.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            Empresa.objects.create(
                nombre='Otro Taller',
                direccion='Otra dirección',
                mision='Otra misión',
                vision='Otra visión',
                anio_fundacion=2015,
                ruc='20123456789'  # Same RUC
            )

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        empresa = Empresa.objects.create(**self.valid_data)
        expected_url = reverse('empresa:detail', kwargs={'pk': empresa.pk})
        self.assertEqual(empresa.get_absolute_url(), expected_url)

    def test_imagen_field_optional(self):
        """Test that imagen field is optional"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertIsNone(empresa.imagen.name)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Empresa._meta.verbose_name, 'Empresa')
        self.assertEqual(Empresa._meta.verbose_name_plural, 'Empresas')

    def test_anio_fundacion_as_integer(self):
        """Test that anio_fundacion accepts integers"""
        empresa = Empresa.objects.create(**self.valid_data)
        self.assertIsInstance(empresa.anio_fundacion, int)
        self.assertEqual(empresa.anio_fundacion, 2010)
