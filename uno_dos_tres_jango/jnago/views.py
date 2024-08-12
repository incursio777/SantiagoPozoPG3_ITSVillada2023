from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import requests

def hola(request):
    return HttpResponse("Hola mundo")

# Create your views here.
def template(request):
    uri = "https://apis.datos.gob.ar/georef/api/provincias?campos=id, nombre&orden=id"
    response1 = requests.get(uri)
    data = response1.json()
    provincias = data["provincias"]



    t1 = open("C:/Users/Santiago/Downloads/SantiagoPozoPG3_ITSVillada2023/uno_dos_tres_jango/plantillas/template1.html")
    plantilla = Template(t1.read())
    t1.close()
    ctx = Context({"provincias": provincias})
    documento = plantilla.render(ctx)
    return HttpResponse(documento)