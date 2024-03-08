def vocales(palabra):
    voc = 0
    for i in range(len(palabra)):
        if palabra[i] == "a" or palabra[i] == "e" or palabra[i] == "i" or palabra[i] == "o" or palabra[i] == "u":
            voc += 1
    return voc

palabra = str(input("dime una palabra: "))
facts = vocales(palabra)
print(facts)