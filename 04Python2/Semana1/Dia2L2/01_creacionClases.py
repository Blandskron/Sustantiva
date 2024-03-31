# Ejemplo 2: Definición de una clase llamada Persona
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

    def presentarse(self):
        """
        Método que devuelve una cadena de texto con la presentación de la persona.
        :return: Cadena de texto con la presentación de la persona.
        """
        return f'Hola, me llamo {self.nombre} y tengo {self.edad} años.'


# Ejemplo de uso de la clase Persona
persona1 = Persona("Juan", 30)
print(persona1.presentarse())  # Salida: Hola, me llamo Juan y tengo 30 años.
