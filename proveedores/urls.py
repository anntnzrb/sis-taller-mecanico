from django.urls import path
from . import views

app_name = "proveedores"

urlpatterns = [
    path("", views.ProveedorListView.as_view(), name="list"),
    path("agregar/", views.ProveedorCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ProveedorDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", views.ProveedorUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.ProveedorDeleteView.as_view(), name="delete"),
]
