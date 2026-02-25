def longitud(palabra):
    return len(palabra)

palabras = ['Table', 'Chairs', 'Flowers']
longitudes = list(map(longitud, palabras))

print(palabras)
print(longitudes)