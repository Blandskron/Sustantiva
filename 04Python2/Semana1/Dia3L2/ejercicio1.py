class Persona:
    # Método constructor (__init__) que inicializa los atributos nombre, edad y altura
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre  # Asigna el nombre proporcionado al atributo nombre
        self.edad = edad      # Asigna la edad proporcionada al atributo edad
        self.altura = altura  # Asigna la altura proporcionada al atributo altura

    # Método getter para obtener el nombre de la persona
    def get_nombre(self):
        return self.nombre  # Devuelve el valor del atributo nombre

    # Método setter para establecer el nombre de la persona
    def set_nombre(self, nombre):
        self.nombre = nombre  # Establece el valor del atributo nombre con el valor proporcionado

    # Método getter para obtener la edad de la persona
    def get_edad(self):
        return self.edad  # Devuelve el valor del atributo edad

    # Método setter para establecer la edad de la persona
    def set_edad(self, edad):
        self.edad = edad  # Establece el valor del atributo edad con el valor proporcionado

    # Método getter para obtener la altura de la persona
    def get_altura(self):
        return self.altura  # Devuelve el valor del atributo altura

    # Método setter para establecer la altura de la persona
    def set_altura(self, altura):
        self.altura = altura  # Establece el valor del atributo altura con el valor proporcionado


# Creación de una instancia de la clase Persona con nombre "Juan Pérez", edad 30, altura 1.75
persona = Persona("Juan Pérez", 30, 1.75)

# Acceso a los datos de la persona utilizando los métodos de la clase
print("Nombre de la persona:", persona.get_nombre())  # Imprime el nombre de la persona
print("Edad de la persona:", persona.get_edad())      # Imprime la edad de la persona
print("Altura de la persona:", persona.get_altura())  # Imprime la altura de la persona
