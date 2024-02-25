class Cerebro:
    def __init__(self, tipo):
        self.tipo = tipo

    def procesar_informacion(self):
        print(f"Procesando información con el {self.tipo} del cerebro.")


class Neocortex(Cerebro):
    def __init__(self):
        super().__init__("neocórtex")

    def pensar_abstractamente(self):
        print("Pensando abstractamente con el neocórtex.")


class Reptiliano(Cerebro):
    def __init__(self):
        super().__init__("cerebro reptiliano")

    def controlar_instintos(self):
        print("Controlando instintos con el cerebro reptiliano.")
