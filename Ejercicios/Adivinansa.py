import random

number = random.randint(1, 11)
gueess = int(input("Elige Un Numero Del 1 al 10: "))
gueess = int(gueess)

if gueess == number:
    print("Ganaste")
else:
    print("Intentalo De Nuevo")