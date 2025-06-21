from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Empresa


class EmpresaView(TemplateView):
    template_name = "empresa/nosotros.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["empresa"] = Empresa.objects.first()
        return context


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = [
        "nombre",
        "direccion",
        "mision",
        "vision",
        "anio_fundacion",
        "ruc",
        "imagen",
    ]
    template_name = "empresa/form.html"
    success_url = reverse_lazy("empresa:nosotros")


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = "empresa/detail.html"
    context_object_name = "empresa"


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = [
        "nombre",
        "direccion",
        "mision",
        "vision",
        "anio_fundacion",
        "ruc",
        "imagen",
    ]
    template_name = "empresa/form.html"
    success_url = reverse_lazy("empresa:nosotros")
