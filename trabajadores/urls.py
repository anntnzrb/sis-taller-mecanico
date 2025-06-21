from django.urls import path
from . import views

app_name = "trabajadores"

urlpatterns = [
    path("", views.TrabajadorListView.as_view(), name="list"),
    path("agregar/", views.TrabajadorCreateView.as_view(), name="create"),
    path("<int:pk>/", views.TrabajadorDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", views.TrabajadorUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.TrabajadorDeleteView.as_view(), name="delete"),
]
