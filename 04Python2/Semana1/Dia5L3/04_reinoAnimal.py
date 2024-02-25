class ReinoAnimal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def sonido(self):
        if self.tipo == 'mamífero':
            print(f"El {self.nombre} emite sonidos característicos.")
        elif self.tipo == 'ave':
            print(f"El {self.nombre} emite cantos melodiosos.")
        elif self.tipo == 'reptil':
            print(f"El {self.nombre} emite siseos y gruñidos.")


# Uso de la clase
perro = ReinoAnimal("Perro", "mamífero")
perro.sonido()
