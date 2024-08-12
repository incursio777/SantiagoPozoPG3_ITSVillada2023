from django.contrib import admin
from .models import *
# Register your models here.


modules = [    
    Tipodocumento,
    Usuario,
    Turno,
    Carrera,
    Materia,
    Curso,
    Correlatividad,
    EstadoCurso,
    Historial,
    NotaEvaluacion,
    Profesor,
    Inscripcion,
    CondicionFinal
]

for i in modules:
    admin.site.register(i)