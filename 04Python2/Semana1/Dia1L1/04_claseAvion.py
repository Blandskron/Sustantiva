class Avion:
    def __init__(self, modelo, capacidad, aerolinea):
        self.modelo = modelo
        self.capacidad = capacidad
        self.aerolinea = aerolinea

# Instanciar un avión
avion_comercial = Avion("Boeing 737", 150, "American Airlines")
print("El avión", avion_comercial.modelo, "de", avion_comercial.aerolinea, "tiene una capacidad de", avion_comercial.capacidad, "pasajeros")
