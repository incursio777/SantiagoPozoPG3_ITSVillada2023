try:
    with open('esfuerzo_padre.txt', 'w') as archivo:
        archivo.write(123)
except ValueError:
    print("No se puede escribir en el archivo")