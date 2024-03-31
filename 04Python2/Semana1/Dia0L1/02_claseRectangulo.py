class Rectangulo:
    def __init__(self, base, altura):
        """
        Constructor de la clase Rectangulo.

        Args:
        - base (float): La longitud de la base del rectángulo.
        - altura (float): La altura del rectángulo.
        """
        self.base = base    # Asigna la longitud de la base al atributo 'base'
        self.altura = altura  # Asigna la altura al atributo 'altura'

    def area(self):
        """
        Método para calcular el área del rectángulo.

        Returns:
        - float: El área del rectángulo calculada como base * altura.
        """
        return self.base * self.altura

    def perimetro(self):
        """
        Método para calcular el perímetro del rectángulo.

        Returns:
        - float: El perímetro del rectángulo calculado como 2 * (base + altura).
        """
        return 2 * (self.base + self.altura)


# Crear instancias de la clase Rectangulo
rectangulo1 = Rectangulo(5, 3)  # Crea una instancia de Rectangulo con base 5 y altura 3
rectangulo2 = Rectangulo(7, 4)  # Crea una instancia de Rectangulo con base 7 y altura 4

# Calcular el área y perímetro de los rectángulos
print(rectangulo1.area())        # Imprime: 15
print(rectangulo2.perimetro())   # Imprime: 22
