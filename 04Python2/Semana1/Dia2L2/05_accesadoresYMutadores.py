# Clase Persona con accesadores y mutadores
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

    def obtener_nombre(self):
        """
        Método para obtener el nombre de la persona.
        :return: Nombre de la persona.
        """
        return self.nombre

    def establecer_edad(self, nueva_edad):
        """
        Método para establecer la edad de la persona.
        :param nueva_edad: Nueva edad de la persona.
        """
        self.edad = nueva_edad


# Ejemplo de uso de accesadores y mutadores
persona = Persona("María", 25)
print("Nombre:", persona.obtener_nombre())  # Salida: Nombre: María
persona.establecer_edad(30)
print("Nueva Edad:", persona.edad)  # Salida: Nueva Edad: 30
