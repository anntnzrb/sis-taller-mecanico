from django.test import TestCase
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Proveedor


class ProveedorModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'nombre': 'Repuestos Automotrices SA',
            'descripcion': 'Proveedor especializado en repuestos y accesorios automotrices',
            'telefono': '+593-2-2345678',
            'pais': 'Ecuador',
            'correo': 'ventas@repuestossa.com',
            'direccion': 'Av. América 456, Quito'
        }

    def test_create_proveedor_with_valid_data(self):
        """Test creating a supplier with valid data"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertEqual(proveedor.nombre, 'Repuestos Automotrices SA')
        self.assertEqual(proveedor.descripcion, 'Proveedor especializado en repuestos y accesorios automotrices')
        self.assertEqual(proveedor.telefono, '+593-2-2345678')
        self.assertEqual(proveedor.pais, 'Ecuador')
        self.assertEqual(proveedor.correo, 'ventas@repuestossa.com')
        self.assertEqual(proveedor.direccion, 'Av. América 456, Quito')

    def test_proveedor_str_method(self):
        """Test string representation of supplier"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertEqual(str(proveedor), 'Repuestos Automotrices SA')

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        expected_url = reverse('proveedores:detail', kwargs={'pk': proveedor.pk})
        self.assertEqual(proveedor.get_absolute_url(), expected_url)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Proveedor._meta.verbose_name, 'Proveedor')
        self.assertEqual(Proveedor._meta.verbose_name_plural, 'Proveedores')

    def test_correo_field_validation(self):
        """Test that correo field accepts valid email"""
        proveedor = Proveedor.objects.create(**self.valid_data)
        self.assertTrue('@' in proveedor.correo)
        self.assertTrue('.' in proveedor.correo)

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
        data['descripcion'] = long_description
        data['direccion'] = long_address
        
        proveedor = Proveedor.objects.create(**data)
        self.assertEqual(proveedor.descripcion, long_description)
        self.assertEqual(proveedor.direccion, long_address)
