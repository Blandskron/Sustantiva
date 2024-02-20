class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Crear instancias de la clase Rectangulo
rectangulo1 = Rectangulo(5, 3)
rectangulo2 = Rectangulo(7, 4)

# Calcular el área y perímetro de los rectángulos
print(rectangulo1.area())       # Imprime: 15
print(rectangulo2.perimetro())  # Imprime: 22
