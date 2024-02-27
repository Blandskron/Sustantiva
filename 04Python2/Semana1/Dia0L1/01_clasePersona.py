class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        
        Args:
        - nombre (str): Nombre de la persona.
        - edad (int): Edad de la persona.
        """
        self.nombre = nombre  # Asigna el nombre de la persona al atributo 'nombre'
        self.edad = edad      # Asigna la edad de la persona al atributo 'edad'

    def saludar(self):
        """
        Método para que la persona salude.
        Imprime un mensaje de saludo con el nombre y la edad de la persona.
        """
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)    # Crea una instancia de Persona con nombre "Juan" y edad 30
persona2 = Persona("María", 25)   # Crea una instancia de Persona con nombre "María" y edad 25

# Acceder a los atributos y métodos de las instancias
print(persona1.nombre)  # Imprime: Juan
print(persona2.edad)    # Imprime: 25
persona1.saludar()       # Imprime: Hola, soy Juan y tengo 30 años.
