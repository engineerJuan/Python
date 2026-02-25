class Persona:

    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def Es_Mayor_De_Edad(self):
         if self.edad >= 18:
             return True
         
persona1 = Persona ('juan', 18, 'Querty')

print("El Nombre Es:", persona1.nombre)

if persona1.Es_Mayor_De_Edad():
    print("Es Mayor De Edad")
else:
    print("ES Menor De Edad")