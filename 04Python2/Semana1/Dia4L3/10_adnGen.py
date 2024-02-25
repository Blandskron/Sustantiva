class ADN:
    def __init__(self, secuencia):
        self.secuencia = secuencia  # Inicializa el atributo secuencia

    def replicarse(self):
        # Método replicarse: Simula el proceso de replicación del ADN
        print("El ADN se está replicando para la transmisión de información genética.")


class Gen:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # Inicializa el atributo nombre del gen
        self.tipo = tipo  # Inicializa el atributo tipo del gen

    def expresarse(self):
        # Método expresarse: Simula el proceso de expresión génica
        print(f"El gen {self.nombre} de tipo {self.tipo} se está expresando.")
