def oredenamientoburbuja(listadesordenada):
    listadesordenada.sort()
    listadesordenada.reverse()
    return listadesordenada

listadesordenada = [10, 5, 9, 1, 4, 7, 8, 2, 6, 3]
orden = oredenamientoburbuja(listadesordenada)
print(orden)