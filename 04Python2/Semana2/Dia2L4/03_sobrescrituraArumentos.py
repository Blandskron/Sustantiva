class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


mi_rectangulo = Rectangulo(5, 10)
print("Área del rectángulo:", mi_rectangulo.area())  # Salida: 50

mi_cuadrado = Cuadrado(5)
print("Área del cuadrado:", mi_cuadrado.area())      # Salida: 25
