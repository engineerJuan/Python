

def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero_ingresado = int(input("Ingrese numero: "))
resultado = par(numero_ingresado)

if resultado:
    print("El número es par.")
else:
    print("El número es impar.")