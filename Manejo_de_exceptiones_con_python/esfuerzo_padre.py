var = "S"
while var == "S":
    try:
        x1 = int (input("Dime un numero: "))
        x2 = int (input("Dime otro numero: "))
    except ValueError:
        print("No se puede ingresar letras")
    finally:
        print(x1+x2)
        var = input("decea repetir la operacion? S/N")
        if var == "N":
            break
        elif var == "S":
            continue
    