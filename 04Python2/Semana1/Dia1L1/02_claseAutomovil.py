class Automovil:
    def __init__(self, marca, modelo, color):
        """
        Constructor de la clase Automovil.

        Args:
        - marca (str): La marca del automóvil.
        - modelo (str): El modelo del automóvil.
        - color (str): El color del automóvil.
        """
        self.marca = marca    # Asigna la marca proporcionada al atributo 'marca'
        self.modelo = modelo  # Asigna el modelo proporcionado al atributo 'modelo'
        self.color = color    # Asigna el color proporcionado al atributo 'color'

# Instanciar un automóvil
mi_auto = Automovil("Toyota", "Corolla", "Negro")  # Crea una instancia de Automovil con marca Toyota, modelo Corolla y color Negro

# Imprimir la información del automóvil
print("Mi auto es un", mi_auto.marca, mi_auto.modelo, "de color", mi_auto.color)
