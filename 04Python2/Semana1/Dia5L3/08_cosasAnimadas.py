class CosasInanimadas:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def estado(self):
        print(f"La {self.nombre} está hecha de {self.material} y se encuentra en un estado inanimado.")


# Uso de la clase
silla = CosasInanimadas("Silla", "madera")
silla.estado()
