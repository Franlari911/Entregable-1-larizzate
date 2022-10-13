from django.contrib import admin
from django.urls import path, include

from blog.views import mostrar_inicio, busqueda_2,buscar_2, buscar,  busqueda, procesar_formulario

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario/", procesar_formulario, name="formulario"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
     path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar-2/", buscar_2),
    
]
