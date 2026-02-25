class Persona:
    def __init__(self, Nombre):
        self.Nombre = Nombre
    
    def Mostrar_Nombre(self):
        print(self.Nombre)

class Estudiante(Persona):
    def __init__(self, Nombre):
        super().__init__(Nombre)
        
    def Mostrar(self):
        super().Mostrar_Nombre()

Estudiante1 = Estudiante('Juan')
Estudiante1.Mostrar()