class Estudiante:
    def __init__(self, nombre, edad, carrera):
        """
        Constructor de la clase Estudiante.

        Args:
        - nombre (str): El nombre del estudiante.
        - edad (int): La edad del estudiante.
        - carrera (str): La carrera que estudia el estudiante.
        """
        self.nombre = nombre    # Asigna el nombre del estudiante al atributo 'nombre'
        self.edad = edad        # Asigna la edad del estudiante al atributo 'edad'
        self.carrera = carrera  # Asigna la carrera del estudiante al atributo 'carrera'

    def estudiar(self):
        """
        Método que simula que el estudiante está estudiando.
        Imprime un mensaje indicando el nombre del estudiante y su carrera.
        """
        print(f"{self.nombre} está estudiando en la carrera de {self.carrera}.")


# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("Ana", 20, "Ingeniería Civil")  # Crea una instancia de Estudiante con nombre Ana, edad 20 y carrera Ingeniería Civil
estudiante2 = Estudiante("Pedro", 22, "Medicina")         # Crea una instancia de Estudiante con nombre Pedro, edad 22 y carrera Medicina

# Acceder a los atributos y métodos de las instancias
print(estudiante1.edad)         # Imprime: 20
print(estudiante2.carrera)       # Imprime: Medicina
estudiante1.estudiar()           # Imprime: Ana está estudiando en la carrera de Ingeniería Civil.
