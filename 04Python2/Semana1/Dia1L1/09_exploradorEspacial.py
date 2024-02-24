class ExploradorEspacial:
    def __init__(self, nombre, mision):
        self.nombre = nombre
        self.mision = mision

    def despegar(self):
        print(f"¡El explorador espacial {self.nombre} ha despegado para la misión {self.mision}!")

    def recolectar_muestras(self, muestras):
        print(f"El explorador {self.nombre} ha recolectado {muestras} muestras de suelo marciano.")

# Crear una instancia de ExploradorEspacial
perseverance = ExploradorEspacial("Perseverance", "Mars 2020")
perseverance.despegar()
perseverance.recolectar_muestras(10)
