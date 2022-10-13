from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import AutosNuevo, AutosUsado, MotosNueva, MotosUsada

# Create your views here.


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")

def inicio (request):
    
    FiatCronos = AutosNuevo(
        marca="Fiat", modelo="Cronos", version="Drive",fecha_de_fabricacion="2022-01-03", color="blanco"
        
    )
    FiatCronos.save()
  
    
    Peugeot208 = AutosUsado(
        marca="Peugeot", modelo="208", version="Active",fecha_de_fabricacion="2020-01-03", color="azul",fecha_de_patentacion="2020-08-07"
        
    )
    Peugeot208.save()
    
    Bmwgs700f = MotosNueva(
        marca="Bmw", modelo="GS700F",cilindrada="700",fecha_de_fabricacion="2022-01-03", color="rojo"
        
    )
    Bmwgs700f.save()
    
    
    Bmwgs800f = MotosUsada(
        marca="Bmw", modelo="GS900F",cilindrada="800",fecha_de_patentacion="2020-01-03",fecha_de_fabricacion="2019-01-03", color="negro"
        
    )
    Bmwgs800f.save()  
      
    contexto = {
        "fiatCronos": FiatCronos,
        "Peugeot208": Peugeot208,
        "Bmwgs700": Bmwgs700f,
        "Bmwgs800": Bmwgs800f
        }

    return render(request, "blog/inicio.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blog/formulario.html")
    
    auto = AutosNuevo(marca=request.POST["marca"], modelo=request.POST["modelo"])
    auto.save()
    return render(request, "blog/inicio.html")


def busqueda(request):
    return render(request, "blog/busqueda.html")


def buscar(request):
    respuesta = f"Buscando la marca : {request.GET['marca']}"
    return HttpResponse(respuesta) 



def busqueda_2(request):
    return render(request, "blog/busqueda_2.html")


def buscar_2(request):

    if not request.GET["marca"]:
        return HttpResponse("No enviaste datos")
    else:
        marca_a_buscar = request.GET["marca"]
        AutosNuevos = AutosNuevo.objects.filter(marca=marca_a_buscar)

        contexto = {"marca": marca_a_buscar, "AutosNuevos_encontrados": AutosNuevos}

        return render(request, "blog/resultado_busqueda.html", contexto)




