from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string




class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Turno(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Usuario(AbstractUser):
    tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE, null=True)
    documento = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateField(null=True)
    carrera = models.ManyToManyField(Carrera, null=True, default='')


class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    siglas = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    materia_correlativa = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    nombreCurso = models.CharField(max_length=255)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    nivel = models.IntegerField()
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default='')
    listaHorarios = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreCurso
    

class EstadoCurso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Correlatividad(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estado_curso = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)


class Profesor(models.Model):
    nombre = models.CharField(max_length=255, default='')
    apellido = models.CharField(max_length=255, default='')
    correo = models.EmailField(default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class CondicionFinal(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    condicionFinal = models.ForeignKey(CondicionFinal, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField(null=True)

    def __str__(self):
        return self.curso.nombreCurso + ' ' + self.usuario.username

    def setFechaFinal(self, fechaFinal):    
        self.fechaFinal = fechaFinal

    def generar_codigo_alfanumerico():
        caracteres = string.ascii_letters + string.digits
        codigo = ''.join(random.choice(caracteres) for _ in range(15))
        return codigo

class NotaEvaluacion(models.Model):
    nombre = models.CharField(max_length=255)
    tipoEvaluacion = models.CharField(max_length=255)
    valor = models.IntegerField()
    fecha = models.DateField()
    Inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, default='')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    Inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, default='')
    estado_curso = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)

class HorarioClase(models.Model):
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    asignatura = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.dia_semana} - {self.hora_inicio} a {self.hora_fin}"

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.IntegerField()
    campo3 = models.BooleanField(default=False)

    def __str__(self):
        return self.campo1
    
class Horario:
    def __init__(self, dia, turno, actividad):
        self.dia = dia
        self.turno = turno
        self.actividad = actividad

'''class HorarioClase:
    def __init__(self):
        self.horarios = []

    def agregar_horario(self, dia, turno, actividad):
        horario = Horario(dia, turno, actividad)
        self.horarios.append(horario)

    def mostrar_horarios(self):
        for horario in self.horarios:
            print(f"{horario.dia} - {horario.turno}: {horario.actividad}")

#ejem
horarios_semana = HorarioClase()

#agregar
horarios_semana.agregar_horario("Lunes", "Mañana", "Clase de Matemáticas")
horarios_semana.agregar_horario("Martes", "Tarde", "Reunión de equipo")
horarios_semana.agregar_horario("Miércoles", "Noche", "Estudio individual")
horarios_semana.agregar_horario("Jueves", "Mañana", "Clase de Historia")

#ver
horarios_semana.mostrar_horarios()'''
