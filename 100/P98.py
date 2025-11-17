def escribir(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

escribir('P98.html', 'conexion de python a html')