numero = int(input("Ingresa Un Numero:"))
factorial = 1
i = 1

while i <= numero:
    factorial = factorial * i
    i = i + 1
print("El Factorial Es: ", factorial)