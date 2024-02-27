class Perro:
    def __init__(self, nombre, raza, edad):
        """
        Constructor de la clase Perro.

        Args:
        - nombre (str): El nombre del perro.
        - raza (str): La raza del perro.
        - edad (int): La edad del perro.
        """
        self.nombre = nombre  # Asigna el nombre proporcionado al atributo 'nombre'
        self.raza = raza      # Asigna la raza proporcionada al atributo 'raza'
        self.edad = edad      # Asigna la edad proporcionada al atributo 'edad'

# Instanciar un perro
mi_perro = Perro("Buddy", "Labrador", 3)  # Crea una instancia de Perro con nombre Buddy, raza Labrador y edad 3 años

# Imprimir la información del perro
print("Mi perro se llama", mi_perro.nombre, "es de raza", mi_perro.raza, "y tiene", mi_perro.edad, "años")
