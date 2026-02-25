class Coche:
    
    def __init__(self, marca, modelo, matricula, kilometros):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.kilometros = kilometros

    def avanzar(self, kilometros):
        self.kilometros = self.kilometros + kilometros 

coche1 = Coche('Mclaren', '765 LT', '101 010', 1000)
print(coche1.__dict__)

coche1.avanzar(1000)
print(coche1.__dict__)