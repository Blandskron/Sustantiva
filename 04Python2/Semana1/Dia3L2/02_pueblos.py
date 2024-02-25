class Pueblos:
    def __init__(self, continente):
        """
        Constructor de la clase Pueblos.

        Args:
        - continente (str): El continente al que pertenecen los pueblos históricos.
        """
        self.continente = continente

    class Historicos:
        def __init__(self, nombre):
            """
            Constructor de la clase Historicos.

            Args:
            - nombre (str): El nombre del pueblo histórico.
            """
            self.nombre = nombre

# Ejemplo de uso
pueblos = Pueblos("Europa")
romanos = pueblos.Historicos("Romanos")
vikingos = pueblos.Historicos("Vikingos")
print(f"Continente: {pueblos.continente}")
print(f"Pueblo histórico 1: {romanos.nombre}")
print(f"Pueblo histórico 2: {vikingos.nombre}")
