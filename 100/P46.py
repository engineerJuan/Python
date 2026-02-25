numero = int(input('Ingresa el numero:'))
contador = 0

while numero != 0:
    numero = numero // 10
    contador = contador +1

print("Los digitos son: ", contador)