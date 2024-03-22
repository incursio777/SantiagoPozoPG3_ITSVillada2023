class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def tarea(self):
        print("hola soy "+self.nombre+" y tengo "+str(self.edad)+" años")

class paco(persona):
    def tarea(self):
        return super().tarea()

class pepe(persona):
    def tarea(self):
        return super().tarea()

persona1 = paco("paco",20)
persona1.tarea()
persona2 = pepe("pepe",15)
persona2.tarea()
