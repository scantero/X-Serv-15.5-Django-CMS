from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def mostrarContenido(request):
    paginas = Pages.objects.all()
    respuesta = "<ul>"
    for pagina in paginas:
        respuesta += '<li><a href="/'+ str(pagina.id) + '">' + pagina.name + ': ' + pagina.page + '</a></li>'
        #respuesta += '<li>' + pagina.name + ": " + pagina.page
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

def notfound(request):
    respuesta = "<ul>Usos de la aplicacion:"
    respuesta += "<li>La pagina principal te muestra todos los contenidos diponibles"
    respuesta += "<li>/(identificador): devuelve el contenido correspondiente"
    respuesta += "<li>/nuevocontenido/(name)/(page): crea un nuevo contenido</li>"
    respuesta += '<br><a href="http://localhost:8000">Vuelve a la pagina principal</a></ul>'
    return HttpResponse(respuesta)
