class Coche:
    def __init__(self, marca):
        """
        Constructor de la clase Coche.

        Args:
        - marca (str): La marca del coche.
        """
        self.marca = marca     # Asigna la marca del coche al atributo 'marca'
        self.ruedas = Ruedas() # Instancia de la clase Ruedas para representar las ruedas del coche
        self.motor = Motor()   # Instancia de la clase Motor para representar el motor del coche
        self.chasis = Chasis() # Instancia de la clase Chasis para representar el chasis del coche

class Ruedas:
    def __init__(self):
        """Constructor de la clase Ruedas."""
        self.tipo = "Verano"  # Por defecto, el tipo de ruedas es "Verano"

class Motor:
    def __init__(self):
        """Constructor de la clase Motor."""
        self.tipo = "Gasolina"  # Por defecto, el tipo de motor es "Gasolina"

class Chasis:
    def __init__(self):
        """Constructor de la clase Chasis."""
        self.material = "Acero"  # Por defecto, el material del chasis es "Acero"
