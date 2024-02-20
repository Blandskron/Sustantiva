import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Crear una instancia de Circulo
circulo1 = Circulo(5)
print("Área del círculo:", circulo1.calcular_area())
print("Perímetro del círculo:", circulo1.calcular_perimetro())
