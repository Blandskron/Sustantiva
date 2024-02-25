class Cerebro:
    def __init__(self, tipo):
        self.tipo = tipo  # Inicialización del tipo de cerebro

    def procesar_informacion(self):
        # Método para procesar información con el tipo de cerebro
        print(f"Procesando información con el {self.tipo} del cerebro.")


class Neocortex(Cerebro):
    def __init__(self):
        super().__init__("neocórtex")  # Inicialización específica para el neocórtex

    def pensar_abstractamente(self):
        # Método específico para el neocórtex que permite pensar abstractamente
        print("Pensando abstractamente con el neocórtex.")


class Reptiliano(Cerebro):
    def __init__(self):
        super().__init__("cerebro reptiliano")  # Inicialización específica para el cerebro reptiliano

    def controlar_instintos(self):
        # Método específico para el cerebro reptiliano que controla instintos
        print("Controlando instintos con el cerebro reptiliano.")
