class Persona:

    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nueva_nombre):
        self.nombre = nueva_nombre

    @property
    def edad(self):
        return self.edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self.edad = nueva_edad
    
    def mostrar(self):
        print(self.__dict__)
    
    def Mayor_De_Edad(self):
        if self._edad >= 18:
            print("Es Mayor De Edad")
        else:
            print("Es Menor De Edad")
        
Persona1 = Persona('juan', 18)

print(Persona1.Mayor_De_Edad())
Persona1.mostrar()