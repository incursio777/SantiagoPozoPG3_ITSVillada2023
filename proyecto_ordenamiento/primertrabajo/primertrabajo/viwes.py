from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
import requests

def template(request):
    uri = "https://apis.datos.gob.ar/georef/api/provincias?campos=id, nombre&orden=id"
    response1 = requests.get(uri)
    data = response1.json()
    provincias = data["provincias"]



    t1 = open("C:/Users/Santiago/Downloads/SantiagoPozoPG3_ITSVillada2023/proyecto_ordenamiento/primertrabajo/plantillas/template1.html")
    plantilla = Template(t1.read())
    t1.close()
    ctx = Context({"provincias": provincias})
    documento = plantilla.render(ctx)
    return HttpResponse(documento)