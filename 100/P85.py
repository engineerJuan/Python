def contar(palabra):
  return sum(1 for letra in palabra if letra.lower() in 'a e i o u')

palabras = ['rice', 'soup', 'pasta', 'beans', 'bread']
conteos = list(map(contar, palabras))

print(palabras)
print(conteos)