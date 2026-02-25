lista_prueba = [10, 20, 30, 40, 50]

def suma_numeros(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

print("La suma de los números en la lista es:", suma_numeros(lista_prueba))