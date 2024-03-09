def step (numero):
    for i in range(len(numero) - 1):
        n1 = int(numero[i])
        n2 = int(numero[i+1])
        if n1 + 1 == n2 or n1 - 1 == n2: 
            pass
        else:
            return False
    return True


numero = str(input("dime un numero: "))
facts = step(numero)
print(facts)