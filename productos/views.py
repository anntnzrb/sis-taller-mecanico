from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Producto
from .forms import ProductoForm


class ProductoListView(ListView):
    model = Producto
    template_name = "productos/list.html"
    context_object_name = "productos"


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:list")


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:list")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/confirm_delete.html"
    success_url = reverse_lazy("productos:list")
