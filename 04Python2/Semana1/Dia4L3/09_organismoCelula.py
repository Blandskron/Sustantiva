class Organismo:
    # Definición de la clase Organismo
    def __init__(self, nombre, especie):
        # Constructor de la clase Organismo que inicializa los atributos nombre y especie
        self.nombre = nombre  # Atributo para almacenar el nombre del organismo
        self.especie = especie  # Atributo para almacenar la especie del organismo

    def reproducirse(self):
        # Método reproducirse: Imprime un mensaje indicando que el organismo se está reproduciendo
        print(f"{self.nombre} de la especie {self.especie} se está reproduciendo.")


class Celula:
    # Definición de la clase Celula
    def __init__(self, tipo, funcion):
        # Constructor de la clase Celula que inicializa los atributos tipo y funcion
        self.tipo = tipo  # Atributo para almacenar el tipo de célula
        self.funcion = funcion  # Atributo para almacenar la función de la célula

    def dividirse(self):
        # Método dividirse: Imprime un mensaje indicando que la célula se está dividiendo para cumplir su función
        print(f"Una célula de tipo {self.tipo} se está dividiendo para cumplir su función: {self.funcion}.")
