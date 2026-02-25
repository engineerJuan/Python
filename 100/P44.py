import random

Numero_Secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input('adivina El Numero:'))
    intentos = intentos + 1
    
    if intento == Numero_Secreto:
      print(f"Ganaste! te tomo {intentos} intentos")
      break