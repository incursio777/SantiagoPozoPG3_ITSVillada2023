def palindromo(palabra):
    for i in range(len(palabra)):
        if palabra[i] == palabra[len(palabra) - 1 - i]:
            pass
        else:
            return False
    return True


palabra = str(input("dime una palabra: "))
facts = palindromo(palabra)
print(facts)