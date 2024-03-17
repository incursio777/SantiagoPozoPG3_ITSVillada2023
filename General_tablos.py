class persona():

    def inicializar (self,nombre):
        self.nombre=nombre
        self.imprimir()

    def imprimir(self):
        print("Nombre:",self.nombre)

persona1=persona()
persona1.inicializar("sanrra")
persona2=persona()
persona2.inicializar("joagod")