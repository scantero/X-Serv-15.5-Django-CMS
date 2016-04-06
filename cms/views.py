from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def mostrarContenido(request):
    paginas = Pages.objects.all()
    respuesta = "<ul>"
    for pagina in paginas:
        respuesta += '<li>' + pagina.name + ": " + pagina.page
    respuesta += "</ul>"
    return HttpResponse(respuesta)

def mostrarPagina(request, identificador):
    pagina = Pages.objects.get(id=int(identificador))
    respuesta = "<ul>"
    respuesta += '<li><a href:"' + pagina.name + '">' + pagina.page + '</a>'
    respuesta += "</ul>"
    return HttpResponse(respuesta)

@csrf_exempt
def nuevoContenido(request, name, page):
    pagina = Pages(name=name, page=page)
    pagina.save()
    respuesta = "Nuevo contenido guardado con exito"
    return HttpResponse(respuesta)
