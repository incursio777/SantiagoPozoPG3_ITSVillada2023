class pepi:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        print(self.suma())
        print(self.resta())
        print(self.multiplicacion())
        print(self.division())
        
    
    def suma (self):
        return self.n1 + self.n2
    
    def resta (self):
        return self.n1 - self.n2
    
    def multiplicacion (self):
        return self.n1 * self.n2
    
    def division (self):
        return self.n1 / self.n2
    
numeros= pepi(2,3)
