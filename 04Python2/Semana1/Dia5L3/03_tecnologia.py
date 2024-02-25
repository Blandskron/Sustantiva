class Tecnologia:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicialización del nombre de la tecnología

    def desarrollar(self):
        # Método para indicar el desarrollo de nuevas tecnologías en un campo específico
        print(f"Desarrollando nuevas tecnologías en el campo de {self.nombre}.")


class Internet(Tecnologia):
    def __init__(self):
        super().__init__("Internet")  # Llama al inicializador de la clase padre con el nombre "Internet"

    def conectar(self):
        # Método para conectar personas de todo el mundo a través de Internet
        print("Conectando personas de todo el mundo a través de Internet.")
