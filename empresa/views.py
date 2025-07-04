from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Empresa
from .forms import EmpresaForm


class EmpresaView(TemplateView):
    template_name = "empresa/nosotros.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["empresa"] = Empresa.objects.first()
        return context


class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "empresa/form.html"
    success_url = reverse_lazy("empresa:nosotros")


class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = "empresa/form.html"
    success_url = reverse_lazy("empresa:nosotros")
