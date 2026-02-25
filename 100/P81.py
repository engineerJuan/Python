def cuadrado(x):
    return x **2

numeros = [3, 6, 9, 12, 15] 
cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(cuadrados)