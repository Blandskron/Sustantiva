# Ejemplo 1: Definición de una clase simple llamada Punto
class Punto:
    """
    Esta clase representa un punto en un plano cartesiano.
    """

    def __init__(self, x, y):
        """
        Constructor de la clase Punto.
        :param x: Coordenada x del punto.
        :param y: Coordenada y del punto.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Método para representar el punto como una cadena de texto.
        :return: Representación en cadena del punto.
        """
        return f'({self.x}, {self.y})'


# Ejemplo de uso de la clase Punto
p = Punto(3, 4)
print("Coordenadas del punto p:", p)  # Salida: Coordenadas del punto p: (3, 4)
