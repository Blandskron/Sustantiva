class Ordenador:
    def __init__(self, marca):
        """
        Constructor de la clase Ordenador.

        Args:
        - marca (str): La marca del ordenador.
        """
        self.marca = marca
        self.raton = Raton()       # Instancia de la clase Raton para representar el ratón del ordenador
        self.monitor = Monitor()   # Instancia de la clase Monitor para representar el monitor del ordenador
        self.teclado = Teclado()   # Instancia de la clase Teclado para representar el teclado del ordenador
        self.torre = Torre()       # Instancia de la clase Torre para representar la torre del ordenador

class Raton:
    def __init__(self):
        """Constructor de la clase Raton."""
        self.tipo = "Inalámbrico"  # Por defecto, el tipo de ratón es "Inalámbrico"

class Monitor:
    def __init__(self):
        """Constructor de la clase Monitor."""
        self.tipo = "LCD"  # Por defecto, el tipo de monitor es "LCD"

class Teclado:
    def __init__(self):
        """Constructor de la clase Teclado."""
        self.tipo = "QWERTY"  # Por defecto, el tipo de teclado es "QWERTY"

class Torre:
    def __init__(self):
        """Constructor de la clase Torre."""
        self.tarjeta_grafica = TarjetaGrafica()  # Instancia de la clase TarjetaGrafica para representar la tarjeta gráfica de la torre
        self.unidad_optica = UnidadOptica()      # Instancia de la clase UnidadOptica para representar la unidad óptica de la torre
        self.ram = RAM()                          # Instancia de la clase RAM para representar la memoria RAM de la torre
        self.disco_duro = DiscoDuro()            # Instancia de la clase DiscoDuro para representar el disco duro de la torre

class TarjetaGrafica:
    def __init__(self):
        """Constructor de la clase TarjetaGrafica."""
        self.modelo = "NVIDIA"  # Por defecto, el modelo de tarjeta gráfica es "NVIDIA"

class UnidadOptica:
    def __init__(self):
        """Constructor de la clase UnidadOptica."""
        self.tipo = "DVD"  # Por defecto, el tipo de unidad óptica es "DVD"

class RAM:
    def __init__(self):
        """Constructor de la clase RAM."""
        self.capacidad = "8 GB"  # Por defecto, la capacidad de RAM es "8 GB"

class DiscoDuro:
    def __init__(self):
        """Constructor de la clase DiscoDuro."""
        self.capacidad = "1 TB"  # Por defecto, la capacidad de disco duro es "1 TB"
