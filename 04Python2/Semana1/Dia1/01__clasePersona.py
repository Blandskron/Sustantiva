class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Acceder a los atributos y métodos de las instancias
print(persona1.nombre)  # Imprime: Juan
print(persona2.edad)    # Imprime: 25
persona1.saludar()       # Imprime: Hola, soy Juan y tengo 30 años.
