class Avion:
    def __init__(self, modelo, capacidad, aerolinea):
        """
        Constructor de la clase Avion.

        Args:
        - modelo (str): El modelo del avión.
        - capacidad (int): La capacidad del avión (número de pasajeros).
        - aerolinea (str): La aerolínea a la que pertenece el avión.
        """
        self.modelo = modelo        # Asigna el modelo proporcionado al atributo 'modelo'
        self.capacidad = capacidad  # Asigna la capacidad proporcionada al atributo 'capacidad'
        self.aerolinea = aerolinea  # Asigna la aerolínea proporcionada al atributo 'aerolinea'

# Instanciar un avión
avion_comercial = Avion("Boeing 737", 150, "American Airlines")  # Crea una instancia de Avion con modelo Boeing 737, capacidad 150 y aerolínea American Airlines

# Imprimir la información del avión
print("El avión", avion_comercial.modelo, "de", avion_comercial.aerolinea, "tiene una capacidad de", avion_comercial.capacidad, "pasajeros")
