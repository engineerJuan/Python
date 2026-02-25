class libro:
    def __init__(self, Titulo, Autor, Editorial, Anio_publicacion):

        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.Anio_publicacion = Anio_publicacion

mi_libro = libro('Python', 'Juan Pablo', 'no', '2025')  

print(mi_libro.__dict__)  