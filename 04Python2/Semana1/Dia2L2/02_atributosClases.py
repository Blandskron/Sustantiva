# Clase Persona con definición de atributos
class Persona:
    """
    Esta clase representa una persona con nombre, edad y género.
    """

    def __init__(self, nombre, edad, genero):
        """
        Constructor de la clase Persona.
        :param nombre: Nombre de la persona.
        :param edad: Edad de la persona.
        :param genero: Género de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self):
        """
        Método para representar la persona como una cadena de texto.
        :return: Representación en cadena de la persona.
        """
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}'


# Ejemplo de uso de la clase Persona
persona = Persona("Ana", 25, "Femenino")
print(persona)  # Salida: Nombre: Ana, Edad: 25, Género: Femenino
