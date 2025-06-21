from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Trabajador
from .forms import TrabajadorForm


class TrabajadorListView(ListView):
    model = Trabajador
    template_name = "trabajadores/list.html"
    context_object_name = "trabajadores"


class TrabajadorDetailView(DetailView):
    model = Trabajador
    template_name = "trabajadores/detail.html"


class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = "trabajadores/form.html"
    success_url = reverse_lazy("trabajadores:list")


class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = "trabajadores/form.html"
    success_url = reverse_lazy("trabajadores:list")


class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = "trabajadores/confirm_delete.html"
    success_url = reverse_lazy("trabajadores:list")
