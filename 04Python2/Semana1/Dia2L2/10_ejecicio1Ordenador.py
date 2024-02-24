class Ordenador:
    def __init__(self, marca):
        self.marca = marca
        self.raton = Raton()
        self.monitor = Monitor()
        self.teclado = Teclado()
        self.torre = Torre()

class Raton:
    def __init__(self):
        self.tipo = "Inalámbrico"  # Por defecto, podrían especificarse más atributos

class Monitor:
    def __init__(self):
        self.tipo = "LCD"  # Por defecto, podrían especificarse más atributos

class Teclado:
    def __init__(self):
        self.tipo = "QWERTY"  # Por defecto, podrían especificarse más atributos

class Torre:
    def __init__(self):
        self.tarjeta_grafica = TarjetaGrafica()
        self.unidad_optica = UnidadOptica()
        self.ram = RAM()
        self.disco_duro = DiscoDuro()

class TarjetaGrafica:
    def __init__(self):
        self.modelo = "NVIDIA"  # Por defecto, podrían especificarse más atributos

class UnidadOptica:
    def __init__(self):
        self.tipo = "DVD"  # Por defecto, podrían especificarse más atributos

class RAM:
    def __init__(self):
        self.capacidad = "8 GB"  # Por defecto, podrían especificarse más atributos

class DiscoDuro:
    def __init__(self):
        self.capacidad = "1 TB"  # Por defecto, podrían especificarse más atributos
