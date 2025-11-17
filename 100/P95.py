lista1 = [1, {2, 3}, 4, 5, 6, 7, 8, 9, 10, 'a', 'e', {'i', 'o'}, 'u']
sets = list(filter(lambda x: isinstance(x, set), lista1))

print(lista1)
print(sets)