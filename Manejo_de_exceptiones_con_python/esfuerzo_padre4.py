try:
    num1 = int(input("Dime un numero: "))
    num2 = int(input("Dime otro numero: "))
    print(num1/num2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("No se puede convertir el valor")