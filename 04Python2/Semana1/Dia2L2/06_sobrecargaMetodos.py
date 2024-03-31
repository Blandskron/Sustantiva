# Clase Calculadora con sobrecarga de método
class Calculadora:
    """
    Esta clase representa una calculadora básica.
    """

    def __init__(self):
        """
        Constructor de la clase Calculadora.
        """
        pass

    def operacion(self, a, b):
        """
        Método para realizar una operación genérica entre dos números.
        """
        return a + b

    def operacion(self, a, b, c):
        """
        Método para realizar una operación genérica entre tres números.
        """
        return a + b + c


# Ejemplo de uso de sobrecarga de método
calculadora = Calculadora()
resultado1 = calculadora.operacion(2, 3)
print("Resultado1:", resultado1)  # Salida: Resultado1: 5
resultado2 = calculadora.operacion(2, 3, 4)
print("Resultado2:", resultado2)  # Salida: Resultado2: 9
