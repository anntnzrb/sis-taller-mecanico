from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Proveedor


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedores/list.html"
    context_object_name = "proveedores"


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedores/detail.html"


class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ["nombre", "descripcion", "telefono", "pais", "correo", "direccion"]
    template_name = "proveedores/form.html"
    success_url = reverse_lazy("proveedores:list")


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ["nombre", "descripcion", "telefono", "pais", "correo", "direccion"]
    template_name = "proveedores/form.html"
    success_url = reverse_lazy("proveedores:list")


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedores/confirm_delete.html"
    success_url = reverse_lazy("proveedores:list")
