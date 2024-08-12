# UTN - Programación III

[Descripcion](#descripcion-del-proyecto)

[Instalacion](#instalacion-y-configuracion)



## Descripcion del Proyecto

El proyecto está diseñado para facilitar el proceso de reinscripción a materias y brindar un seguimiento integral a los alumnos de la Universidad Tecnológica Nacional – Facultad Regional Córdoba. La aplicación web permite a los estudiantes gestionar su inscripción a materias, consultar notas, y obtener información detallada sobre su desempeño académico. A continuacion este esxplicado cada funcion.

### Procedimiento de Reinscripción.
1. Seleccionar la opción "Inscribir a materia".
2. Mostrar materias de la carrera.
3. Seleccionar materia y turno.
4. Mostrar cursos disponibles.

### Detalles de los Cursos
- Nombre identifica nivel y carrera. Ejemplo: 2K7 para segundo nivel de Ingeniería en Sistemas de Información.

### Inscripción y Consulta de Notas
- Al inscribirse, define condición como Inscripto y proporciona código alfanumérico.
- Consulta de notas durante cursado.
- Muestra tipo de evaluación, valor y fecha.

### Condición Final y Reportes
- Consulta condición final al finalizar cursado.
- Condiciones: Regular, Libre, Aprobación directa, Promoción Práctica.
- Carga de condición final por docente con fecha asociada.
- Generación de reporte de materias regulares con condición, curso, materia y fecha.


## Instalacion y Configuracion

### Requisitos Previos

Pipenv requerido:

```bash
    pip install pipenv
```
<hr>


### Creacion Entorno Virtual

Es esencial trabajar en entornos virtuales para evitar problemas potenciales relacionados con las dependencias de bibliotecas y paquetes. Utilizamos el siguiente conjunto de comandos para establecer y activar nuestro entorno virtual:

```bash
    pipenv install //Creacion
    pipenv shell //Ejecucion
```

### Instalacion de los paquetes

Una vez dentro del entorno virtual, procedemos a instalar todos los paquetes necesarios para desarrollar y ejecutar el proyecto. Esto se logra mediante el siguiente comando:

```bash
    pipenv install -r requirements.txt
```


### Iniciar servidor local

Para arrancar el servidor local y visualizar el proyecto, utiliza el siguiente comando:

```bash 
python manage.py runserver
```

Este comando iniciará el servidor y permitirá que accedas al proyecto localmente. Asegúrate de tener tu entorno virtual activado para garantizar un funcionamiento adecuado.
