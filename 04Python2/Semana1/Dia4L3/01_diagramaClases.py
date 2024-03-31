class Animal:
    def __init__(self, nombre, edad):
        # Constructor de la clase Animal
        self.nombre = nombre  # Inicializa el nombre del animal
        self.edad = edad  # Inicializa la edad del animal

    def obtener_nombre(self):
        # Método para obtener el nombre del animal
        return self.nombre

    def obtener_edad(self):
        # Método para obtener la edad del animal
        return self.edad


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Constructor de la clase Perro que hereda de Animal
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.raza = raza  # Inicializa la raza del perro

    def obtener_raza(self):
        # Método para obtener la raza del perro
        return self.raza


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Constructor de la clase Gato que hereda de Animal
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.color = color  # Inicializa el color del gato

    def obtener_color(self):
        # Método para obtener el color del gato
        return self.color


# Creación de instancias de las clases
perro1 = Perro("Rex", 5, "Labrador")
gato1 = Gato("Whiskers", 3, "Blanco y negro")

# Acceso a los métodos y atributos de las clases
print("Nombre del perro:", perro1.obtener_nombre())
print("Edad del perro:", perro1.obtener_edad())
print("Raza del perro:", perro1.obtener_raza())

print("Nombre del gato:", gato1.obtener_nombre())
print("Edad del gato:", gato1.obtener_edad())
print("Color del gato:", gato1.obtener_color())
