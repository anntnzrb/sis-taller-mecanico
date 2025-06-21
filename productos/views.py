from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = "productos/list.html"
    context_object_name = "productos"


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/detail.html"


class ProductoCreateView(CreateView):
    model = Producto
    fields = ["nombre", "descripcion", "precio", "iva", "imagen"]
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:list")


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombre", "descripcion", "precio", "iva", "imagen"]
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:list")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/confirm_delete.html"
    success_url = reverse_lazy("productos:list")
