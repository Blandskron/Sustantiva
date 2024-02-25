class CosasInanimadas:
    def __init__(self, nombre, material):
        self.nombre = nombre  # Nombre de la cosa inanimada
        self.material = material  # Material del que está hecha la cosa inanimada

    def estado(self):
        # Método para imprimir el estado de la cosa inanimada
        print(f"La {self.nombre} está hecha de {self.material} y se encuentra en un estado inanimado.")

# Creación de una instancia de la clase CosasInanimadas para representar una silla de madera
silla = CosasInanimadas("Silla", "madera")

# Llamada al método estado() para imprimir el estado de la silla
silla.estado()
