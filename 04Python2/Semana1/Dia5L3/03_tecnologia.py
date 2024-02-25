class Tecnologia:
    def __init__(self, nombre):
        self.nombre = nombre

    def desarrollar(self):
        print(f"Desarrollando nuevas tecnologías en el campo de {self.nombre}.")


class Internet(Tecnologia):
    def __init__(self):
        super().__init__("Internet")

    def conectar(self):
        print("Conectando personas de todo el mundo a través de Internet.")
