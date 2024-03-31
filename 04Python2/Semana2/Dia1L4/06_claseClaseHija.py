class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Rectangulo(Figura):
    def __init__(self, color, ancho, altura):
        super().__init__(color)
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura


mi_rectangulo = Rectangulo("rojo", 5, 10)
print(mi_rectangulo.area())  # Salida: 50
