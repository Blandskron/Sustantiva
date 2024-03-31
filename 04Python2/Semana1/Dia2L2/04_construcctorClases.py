# Clase Persona con constructor
class Persona:
    """
    Esta clase representa una persona con nombre y edad.
    """

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        :param nombre: Nombre de la persona.
        :param edad: Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad


# Ejemplo de uso del constructor
persona = Persona("Juan", 30)
print("Nombre:", persona.nombre)  # Salida: Nombre: Juan
print("Edad:", persona.edad)  # Salida: Edad: 30
