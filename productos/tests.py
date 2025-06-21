from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from .models import Producto
from .forms import ProductoForm


class ProductoModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "nombre": "Aceite para Motor",
            "descripcion": "Aceite sintético 5W-30 para motores de alto rendimiento",
            "precio": Decimal("45.99"),
            "iva": 15,
        }

    def test_create_producto_with_valid_data(self):
        """Test creating a product with valid data"""
        producto = Producto.objects.create(**self.valid_data)
        self.assertEqual(producto.nombre, "Aceite para Motor")
        self.assertEqual(
            producto.descripcion,
            "Aceite sintético 5W-30 para motores de alto rendimiento",
        )
        self.assertEqual(producto.precio, Decimal("45.99"))
        self.assertEqual(producto.iva, 15)

    def test_producto_str_method(self):
        """Test string representation of product"""
        producto = Producto.objects.create(**self.valid_data)
        self.assertEqual(str(producto), "Aceite para Motor")

    def test_iva_choices_valid_values(self):
        """Test that IVA accepts only 0 or 15"""
        # Test IVA = 0
        data_0_iva = self.valid_data.copy()
        data_0_iva["iva"] = 0
        producto_0 = Producto.objects.create(**data_0_iva)
        self.assertEqual(producto_0.iva, 0)

        # Test IVA = 15
        data_15_iva = self.valid_data.copy()
        data_15_iva["iva"] = 15
        data_15_iva["nombre"] = "Otro Producto"
        producto_15 = Producto.objects.create(**data_15_iva)
        self.assertEqual(producto_15.iva, 15)

    def test_precio_con_iva_property_with_15_percent(self):
        """Test precio_con_iva calculation with 15% IVA"""
        producto = Producto.objects.create(**self.valid_data)
        expected_price = Decimal("45.99") * Decimal("1.15")
        self.assertEqual(producto.precio_con_iva, expected_price)

    def test_precio_con_iva_property_with_0_percent(self):
        """Test precio_con_iva calculation with 0% IVA"""
        data = self.valid_data.copy()
        data["iva"] = 0
        producto = Producto.objects.create(**data)
        expected_price = Decimal("45.99")  # No IVA added
        self.assertEqual(producto.precio_con_iva, expected_price)

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        producto = Producto.objects.create(**self.valid_data)
        expected_url = reverse("productos:list")
        self.assertEqual(producto.get_absolute_url(), expected_url)

    def test_imagen_field_optional(self):
        """Test that imagen field is optional"""
        producto = Producto.objects.create(**self.valid_data)
        self.assertIsNone(producto.imagen.name)

    def test_meta_verbose_names(self):
        """Test model meta verbose names"""
        self.assertEqual(Producto._meta.verbose_name, "Producto")
        self.assertEqual(Producto._meta.verbose_name_plural, "Productos")

    def test_precio_decimal_field(self):
        """Test that precio is a decimal field with correct precision"""
        producto = Producto.objects.create(**self.valid_data)
        self.assertIsInstance(producto.precio, Decimal)
        self.assertEqual(producto.precio, Decimal("45.99"))

    def test_iva_default_value(self):
        """Test that IVA defaults to 15"""
        data = self.valid_data.copy()
        del data["iva"]  # Remove IVA to test default
        producto = Producto.objects.create(**data)
        self.assertEqual(producto.iva, 15)


class ProductoFormTest(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "nombre": "Aceite para Motor",
            "descripcion": "Aceite sintético 5W-30 para motores de alto rendimiento",
            "precio": "45.99",
            "iva": 15,
        }

    def test_form_with_valid_data(self):
        """Test form validation with valid data"""
        form = ProductoForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_form_save_creates_producto(self):
        """Test that form.save() creates a Producto instance"""
        form = ProductoForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        producto = form.save()
        self.assertIsInstance(producto, Producto)
        self.assertEqual(producto.nombre, "Aceite para Motor")

    def test_form_required_fields(self):
        """Test that required fields show validation errors"""
        form = ProductoForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)
        self.assertIn("descripcion", form.errors)
        self.assertIn("precio", form.errors)

    def test_precio_validation_negative(self):
        """Test precio validation for negative values"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["precio"] = "-10.00"
        form = ProductoForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("precio", form.errors)
        self.assertIn("negativo", str(form.errors["precio"]))

    def test_precio_validation_too_high(self):
        """Test precio validation for values too high"""
        invalid_data = self.valid_form_data.copy()
        invalid_data["precio"] = "1000000.00"
        form = ProductoForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("precio", form.errors)
        self.assertIn("demasiado alto", str(form.errors["precio"]))

    def test_precio_validation_valid_range(self):
        """Test precio validation for valid range"""
        valid_data = self.valid_form_data.copy()
        valid_data["precio"] = "999999.99"
        form = ProductoForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_form_widgets_have_css_classes(self):
        """Test that form widgets have CSS classes"""
        form = ProductoForm()
        self.assertIn("form-control", form.fields["nombre"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["descripcion"].widget.attrs["class"])
        self.assertIn("form-control", form.fields["precio"].widget.attrs["class"])

    def test_form_labels_in_spanish(self):
        """Test that form labels are in Spanish"""
        form = ProductoForm()
        self.assertEqual(form.fields["nombre"].label, "Nombre del Producto")
        self.assertEqual(form.fields["descripcion"].label, "Descripción")
        self.assertEqual(form.fields["precio"].label, "Precio (USD)")
        self.assertEqual(form.fields["iva"].label, "IVA")

    def test_iva_choices_in_form(self):
        """Test that IVA field has correct choices"""
        form = ProductoForm()
        iva_choices = form.fields["iva"].choices
        # Should include the model choices (0, 15)
        choice_values = [choice[0] for choice in iva_choices if choice[0] != ""]
        self.assertIn(0, choice_values)
        self.assertIn(15, choice_values)
