def busqueda(numseleccionado, listanumeros):
    for i in listanumeros:
        if i == numseleccionado:
            return("encontrado en la posicon", listanumeros.index(i))
            break
    if i != numseleccionado:
        return("no encontrado") 

listanumeros = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
print("seleccione el numero que desea buscar")
numseleccionado = int(input())
resultado = busqueda(numseleccionado, listanumeros)
print(str(resultado))

