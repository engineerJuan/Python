peso = float(input("Ingresa Tu Peso: "))
altura = float(input("Ingresa Tu Altura: "))

imc = peso / altura ** 2

print(imc)

if imc < 18.5:
    print('Tu Peso Es Bajo')
elif imc < 25:
    print('Tu Peso Es Normal')
elif imc < 30:
    print('Tiene Sobrepeso')
elif imc < 35:
    print('Tiene Obesidad Grado 1')
elif imc < 40:
    print('Tiene Obesidad Grado 2')
else:
    print('Tiene Obesidad Grado 3')