class Hombre:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicialización del nombre del hombre

    def trabajar(self):
        # Método para indicar que el hombre está trabajando para sustentar a su familia
        print(f"{self.nombre} está trabajando para sustentar a su familia.")


class Mujer:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicialización del nombre de la mujer

    def cuidar_hogar(self):
        # Método para indicar que la mujer está cuidando el hogar y la familia
        print(f"{self.nombre} está cuidando el hogar y la familia.")
