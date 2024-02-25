class ADN:
    def __init__(self, secuencia):
        self.secuencia = secuencia

    def replicarse(self):
        print("El ADN se está replicando para la transmisión de información genética.")


class Gen:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def expresarse(self):
        print(f"El gen {self.nombre} de tipo {self.tipo} se está expresando.")
