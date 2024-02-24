class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura


# Creación de una instancia de la clase Persona
persona = Persona("Juan Pérez", 30, 1.75)

# Acceso a los datos de la persona utilizando los métodos de la clase
print("Nombre de la persona:", persona.get_nombre())
print("Edad de la persona:", persona.get_edad())
print("Altura de la persona:", persona.get_altura())
