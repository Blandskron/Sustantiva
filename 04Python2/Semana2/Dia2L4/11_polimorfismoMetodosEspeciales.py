class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Ejemplo de polimorfismo
punto1 = Punto(1, 2)
punto2 = Punto(3, 4)

punto_suma = punto1 + punto2
print(punto_suma)  # Imprime: (4, 6)
