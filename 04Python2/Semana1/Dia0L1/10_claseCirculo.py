import math  # Importa el módulo math para acceder a las constantes y funciones matemáticas

class Circulo:
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.

        Args:
        - radio (float): El radio del círculo.
        """
        self.radio = radio  # Asigna el radio del círculo al atributo 'radio'

    def calcular_area(self):
        """
        Método para calcular el área del círculo.

        Returns:
        - float: El área del círculo.
        """
        return math.pi * self.radio ** 2  # Calcula y devuelve el área del círculo usando la fórmula πr^2

    def calcular_perimetro(self):
        """
        Método para calcular el perímetro del círculo.

        Returns:
        - float: El perímetro del círculo.
        """
        return 2 * math.pi * self.radio  # Calcula y devuelve el perímetro del círculo usando la fórmula 2πr

# Crear una instancia de Circulo con radio 5
circulo1 = Circulo(5)

# Calcular y mostrar el área y el perímetro del círculo
print("Área del círculo:", circulo1.calcular_area())        # Imprime el área del círculo
print("Perímetro del círculo:", circulo1.calcular_perimetro())  # Imprime el perímetro del círculo
