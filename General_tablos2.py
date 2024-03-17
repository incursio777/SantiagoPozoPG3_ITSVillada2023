class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        self.imprimir()
        self.mostrar_estado()

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("sansrra",8)

alumno2=Alumno()
alumno2.inicializar("joagod",1)