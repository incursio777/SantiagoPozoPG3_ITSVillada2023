meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
try:
    mes = int(input("dime un mes: "))
    print(meses[mes - 1])
except ValueError:
    print("el valor introducido no es un numero")
except IndexError:
    print("el valor introducido no es un numero de mes")