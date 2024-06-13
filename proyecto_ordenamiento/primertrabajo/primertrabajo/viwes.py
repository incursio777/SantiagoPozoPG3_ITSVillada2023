from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
import requests


def fecha(request):
    now = datetime.now()

    todo = """<html>
    <body>
    <h1>
    fecha y hora %s
    </h1>
    </body>
    </html>""" % now
    return HttpResponse(todo)

def calculo_url(request, num1, num2):
    n1=int(num1)
    n2=int(num2)
    suma=n1+n2
    todo = """<html>
    <body>
    <h1>
    %s + %s = %s
    </h1>""" % (n1, n2, suma)
    return HttpResponse(todo)

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