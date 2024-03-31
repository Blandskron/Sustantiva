class ReinoVegetal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # Nombre de la planta
        self.tipo = tipo      # Tipo de crecimiento de la planta (rápido, lento, etc.)

    def crecimiento(self):
        # Método para describir el crecimiento de la planta
        print(f"La planta {self.nombre} está experimentando un crecimiento {self.tipo}.")

# Creación de una instancia de la clase ReinoVegetal
arbol = ReinoVegetal("Roble", "rápido")

# Llamada al método crecimiento para describir el crecimiento del roble
arbol.crecimiento()
