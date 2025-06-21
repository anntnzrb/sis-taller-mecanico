from django.urls import path
from . import views

app_name = "empresa"

urlpatterns = [
    path("", views.EmpresaView.as_view(), name="nosotros"),
    path("agregar/", views.EmpresaCreateView.as_view(), name="create"),
    path("<int:pk>/editar/", views.EmpresaUpdateView.as_view(), name="update"),
]
