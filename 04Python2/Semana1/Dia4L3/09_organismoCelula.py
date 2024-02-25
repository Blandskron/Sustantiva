class Organismo:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def reproducirse(self):
        print(f"{self.nombre} de la especie {self.especie} se está reproduciendo.")


class Celula:
    def __init__(self, tipo, funcion):
        self.tipo = tipo
        self.funcion = funcion

    def dividirse(self):
        print(f"Una célula de tipo {self.tipo} se está dividiendo para cumplir su función: {self.funcion}.")
