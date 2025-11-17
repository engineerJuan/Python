import random

while True:
    moneda = random.randint(1, 2)
    if moneda == 1:
        print("Cara")
    else:
        print("Cruz")
    jugar = input("Tirar de nuevo (Si/No): ")
    if jugar.lower() == 'no':
        break

print("Gracias por jugar")