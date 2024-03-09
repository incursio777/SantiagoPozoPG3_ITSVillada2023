año = int(input("dime el año actual : "))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("es bisiesto")
        else:
            print("no es bisiesto")
    else:
        print("es bisiesto")
else:
    print("no es bisiesto")