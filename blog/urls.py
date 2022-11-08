
from multiprocessing import context
from re import template
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import (
    AutosDelete,
    AutosDetalle,
    AutosUpdateView,
    AutosList,
    AutosCreacion,
    busqueda_de_auto,
    listar_autos,
    buscar_auto,
    # clase 23
    MyLogin,
    # MyLogout,
    login_request,
    mostrar_inicio,
    register,
    # clase 24
    editar_perfil,
    agregar_avatar,
)
from django.contrib.auth.views import LogoutView



urlpatterns = [

        # CLASE 22
    path("busqueda-de-Auto/", busqueda_de_auto, name="busqueda"),
    path("buscar-autos/", buscar_auto),
    path("Autos-lista/", listar_autos),
    path("Autos/list", AutosList.as_view(), name="AutosList"),
    # path("r'(?P<pk>\d+)^$'", AutoDetalle.as_view(), name="AutoDetail"),
    path("Auto-nuevo/", AutosCreacion.as_view(), name="AutosNew"),
    path("editar/<pk>", AutosUpdateView.as_view(), name="AutosUpdate"),
    path("borrar/<pk>", AutosDelete.as_view(), name="AutosDelete"),
    # CLASE 23
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("login/", MyLogin.as_view(), name="Login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="blog/logout.html"),
        name="Logout",
    ),
    path("register/", register, name="Register"),
    # Clase 24
    path("Auto/<pk>'", AutosDetalle.as_view(), name="AutosDetail"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    # Clase 25
    path("", mostrar_inicio),
    
]
