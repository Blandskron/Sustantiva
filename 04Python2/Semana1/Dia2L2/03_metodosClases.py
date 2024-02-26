# Clase Calculadora con definición de métodos
class Calculadora:
    """
    Esta clase representa una calculadora básica.
    """

    def __init__(self):
        """
        Constructor de la clase Calculadora.
        """
        pass

    def sumar(self, a, b):
        """
        Método para sumar dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Suma de a y b.
        """
        return a + b

    def restar(self, a, b):
        """
        Método para restar dos números.
        :param a: Primer número.
        :param b: Segundo número.
        :return: Resta de a y b.
        """
        return a - b


# Ejemplo de uso de la clase Calculadora
calculadora = Calculadora()
resultado_suma = calculadora.sumar(5, 3)
print("5 + 3 =", resultado_suma)  # Salida: 5 + 3 = 8
resultado_resta = calculadora.restar(10, 4)
print("10 - 4 =", resultado_resta)  # Salida: 10 - 4 = 6
