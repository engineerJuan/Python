class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo1 = Rectangulo(5, 3)

print(f"Área: {rectangulo1.calcular_area()}")
print(f"Perímetro: {rectangulo1.calcular_perimetro()}")
