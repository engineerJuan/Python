lista = [1,2,3,4,5,6,7,8,9,10]

try:
    print(lista[11])
except IndexError:
    print("Error")