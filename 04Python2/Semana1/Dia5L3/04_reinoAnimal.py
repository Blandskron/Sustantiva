class ReinoAnimal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # Nombre del animal
        self.tipo = tipo      # Tipo de animal (mamífero, ave, reptil)

    def sonido(self):
        # Método para determinar el sonido que emite el animal según su tipo
        if self.tipo == 'mamífero':
            print(f"El {self.nombre} emite sonidos característicos.")
        elif self.tipo == 'ave':
            print(f"El {self.nombre} emite cantos melodiosos.")
        elif self.tipo == 'reptil':
            print(f"El {self.nombre} emite siseos y gruñidos.")

# Creación de una instancia de la clase ReinoAnimal
perro = ReinoAnimal("Perro", "mamífero")

# Llamada al método sonido para determinar el tipo de sonido que emite el perro
perro.sonido()
