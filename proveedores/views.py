from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Proveedor
from .forms import ProveedorForm


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedores/list.html"
    context_object_name = "proveedores"


class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedores/form.html"
    success_url = reverse_lazy("proveedores:list")


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedores/form.html"
    success_url = reverse_lazy("proveedores:list")


class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedores/confirm_delete.html"
    success_url = reverse_lazy("proveedores:list")
