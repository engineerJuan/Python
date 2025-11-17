def promedio(lista):
    return sum(lista) / len(lista)

calificaciones = input("Ingresa calificaciones separadas por comas: ")

numeros = [int(num) for num in calificaciones.split(",")]
resultado = promedio(numeros)

print("Tu promedio es:", resultado)