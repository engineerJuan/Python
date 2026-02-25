import math

class Circulo:
    
    def __init__(self, radio):
            self.radio = radio

    def calcular_Area(self):
          return math.pi * self.radio ** 2
    
    def calcular_Perimetro(self):
        return 2 * math.pi ** self.radio
    
Circulo1 = Circulo(5)

print(f"El Area Es: {Circulo1.calcular_Area()}")          
print(f"Perimetro: {Circulo1.calcular_Perimetro()}")