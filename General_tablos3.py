class triangulo:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    def ladomayor (self):
        if self.n1 > self.n2 and self.n1 > self.n3:
            return self.n1, "es el lado mayor"
        elif self.n2 > self.n1 and self.n2 > self.n3:
            return self.n2, "es el lado mayor"
        elif self.n3 > self.n1 and self.n3 > self.n2:
            return self.n3, "es el lado mayor"
        elif self.n1 == self.n2 and self.n1 == self.n3:
            return "ninguin es el lado mayor"
        
    def equilatero (self):
        if self.n1 == self.n2 and self.n1 == self.n3:
            return "es equilatero"
        else:
            return "no es equilatero"
        
triangulo1 = triangulo(3, 4, 5)
print(triangulo1.ladomayor())
print(triangulo1.equilatero())

triangulo2 = triangulo(3, 3, 3)
print(triangulo2.ladomayor())
print(triangulo2.equilatero())