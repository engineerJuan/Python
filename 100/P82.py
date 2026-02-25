def convertir(x):
    return int(x) 

cadena = ["10", "20", "30", "40", "50"]
entero = list(map(convertir, cadena))

print(cadena)
print(entero)