
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from blog.models import  Avatar, AutosNuevo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import AvatarForm, UserEditionForm



class AutosList(LoginRequiredMixin, ListView):
    model = AutosNuevo
    template_name = "blog/Autos_list.html"


@login_required
def listar_autos(request):
    todos_los_autos = AutosNuevo.objects.all()
    avatar = Avatar.objects.filter(user=request.user).first()
    contexto = {
        "autos_encontrados": todos_los_autos,
        "avatar": avatar.imagen.url
    }

    return render(request, "blog/listar-Autos.html", contexto)


class AutosDetalle(LoginRequiredMixin, DetailView):
    model = AutosNuevo
    template_name = "blog/Auto_detalle.html"


class AutosCreacion(LoginRequiredMixin, CreateView):
    model = AutosNuevo
    fields = ["marca", "modelo"]
    success_url = "/blog/Autos/list"


class AutosUpdateView(LoginRequiredMixin, UpdateView):
    model = AutosNuevo
    success_url = "/blog/Autos/list"
    fields = ["marca", "modelo"]


class AutosDelete(LoginRequiredMixin, DeleteView):

    model = AutosNuevo
    success_url = "/blog/Autos/list"


@login_required
def busqueda_de_auto(request):
    return render(request, "blog/busqueda_de_auto.html")


@login_required
def buscar_auto(request):
    if not request.GET["marca"]:
        return HttpResponse("No enviaste datos")
    else:
        marca_a_buscar = request.GET["marca"]
        AutosNuevos = AutosNuevo.objects.filter(marca=marca_a_buscar)

        contexto = {"marca": marca_a_buscar, "Autos_encontrados": AutosNuevos}

        return render(request, "blog/resultado_busqueda.html", contexto)

###############################################################################
# Clase 23
###############################################################################

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView

class MyLogin(LoginView):
    template_name = "blog/login.html"


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "blog/inicio.html", contexto)


def login_request(request):

    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "blog/login.html", {"form": form})

    form = AuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        return render(
            request,
            "blog/inicio.html",
            {"mensaje": "Error: los datos ingresados no son correctos"},
        )
    else:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(
                request, "blog/inicio.html", {"mensaje": f"Bienvenido {username}"}
            )
        else:
            return render(
                request,
                "blog/inicio.html",
                {"mensaje": "El usuario no existe en nuestra appliación"},
            )


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "blog/registro.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        "avatar": avatar.imagen.url
    }
    return render(request, "blog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)
