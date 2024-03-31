class ExploradorEspacial:
    def __init__(self, nombre, mision):
        """
        Constructor de la clase ExploradorEspacial.

        Args:
        - nombre (str): El nombre del explorador espacial.
        - mision (str): La misión en la que participa el explorador espacial.
        """
        self.nombre = nombre    # Asigna el nombre del explorador espacial al atributo 'nombre'
        self.mision = mision    # Asigna la misión del explorador espacial al atributo 'mision'

    def despegar(self):
        """Método para indicar que el explorador espacial ha despegado."""
        print(f"¡El explorador espacial {self.nombre} ha despegado para la misión {self.mision}!")

    def recolectar_muestras(self, muestras):
        """
        Método para indicar la cantidad de muestras de suelo marciano recolectadas por el explorador.

        Args:
        - muestras (int): La cantidad de muestras recolectadas.
        """
        print(f"El explorador {self.nombre} ha recolectado {muestras} muestras de suelo marciano.")

# Crear una instancia de ExploradorEspacial
perseverance = ExploradorEspacial("Perseverance", "Mars 2020")  # Crea una instancia de ExploradorEspacial con nombre "Perseverance" y misión "Mars 2020"

# Llamar a los métodos de la instancia de ExploradorEspacial
perseverance.despegar()                    # Llama al método despegar para indicar que el explorador Perseverance ha despegado para la misión Mars 2020
perseverance.recolectar_muestras(10)    # Llama al método recolectar_muestras para indicar que el explorador Perseverance ha recolectado 10 muestras de suelo marciano
