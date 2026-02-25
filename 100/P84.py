def suma_cuadrado(x, y):
    return (x + y) ** 2 

list1 = [20, 43, 49, 12, 19]
list2 = [180, 257, 551, 888, 981]

resultdo = list(map(suma_cuadrado, list1, list2))

print(list1)
print(list2)

print(resultdo)