from django.urls import path
from . import views

urlpatterns = [
    path('cargar-municipios/', views.cargar_municipios, name='cargar_municipios'),
    path('seleccionar-estado/', views.seleccionar_estado, name='seleccionar_estado'),
]