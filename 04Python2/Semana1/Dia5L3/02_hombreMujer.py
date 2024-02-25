class Hombre:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        print(f"{self.nombre} está trabajando para sustentar a su familia.")


class Mujer:
    def __init__(self, nombre):
        self.nombre = nombre

    def cuidar_hogar(self):
        print(f"{self.nombre} está cuidando el hogar y la familia.")
