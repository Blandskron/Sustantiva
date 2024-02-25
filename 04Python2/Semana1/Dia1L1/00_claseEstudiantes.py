class Estudiante:
    def __init__(self, nombre, edad, curso):
        """
        Constructor de la clase Estudiante.

        Args:
        - nombre (str): El nombre del estudiante.
        - edad (int): La edad del estudiante.
        - curso (str): El curso al que está inscrito el estudiante.
        """
        self.nombre = nombre    # Asigna el nombre del estudiante al atributo 'nombre'
        self.edad = edad        # Asigna la edad del estudiante al atributo 'edad'
        self.curso = curso      # Asigna el curso del estudiante al atributo 'curso'

    def mostrar_info(self):
        """Método para mostrar la información del estudiante."""
        print(f"Nombre: {self.nombre}")   # Imprime el nombre del estudiante
        print(f"Edad: {self.edad}")       # Imprime la edad del estudiante
        print(f"Curso: {self.curso}")     # Imprime el curso del estudiante

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Ana", 20, "Matemáticas")  # Crea una instancia de Estudiante con nombre Ana, edad 20 y curso Matemáticas
estudiante1.mostrar_info()                          # Llama al método mostrar_info() para imprimir la información del estudiante
