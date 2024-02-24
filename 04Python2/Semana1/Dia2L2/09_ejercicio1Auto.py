class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.ruedas = Ruedas()
        self.motor = Motor()
        self.chasis = Chasis()

class Ruedas:
    def __init__(self):
        self.tipo = "Verano"  # Por defecto, podrían especificarse más atributos

class Motor:
    def __init__(self):
        self.tipo = "Gasolina"  # Por defecto, podrían especificarse más atributos

class Chasis:
    def __init__(self):
        self.material = "Acero"  # Por defecto, podrían especificarse más atributos
