# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Creación de un objeto de la clase Persona
persona1 = Persona("Ana", 30)

# Llamada al método de la clase
persona1.saludar()  # Output: Hola, me llamo Ana y tengo 30 años.
