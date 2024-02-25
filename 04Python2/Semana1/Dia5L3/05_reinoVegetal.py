class ReinoVegetal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def crecimiento(self):
        print(f"La planta {self.nombre} está experimentando un crecimiento {self.tipo}.")


# Uso de la clase
arbol = ReinoVegetal("Roble", "rápido")
arbol.crecimiento()
