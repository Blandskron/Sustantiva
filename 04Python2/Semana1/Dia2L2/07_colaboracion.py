class Profesor:
    def __init__(self, nombre):
        """
        Constructor de la clase Profesor.

        Args:
        - nombre (str): El nombre del profesor.
        """
        self.nombre = nombre  # Asigna el nombre del profesor al atributo 'nombre'

    def enseñar(self):
        """Método para indicar que el profesor está enseñando."""
        return "Enseñando"  # Devuelve un mensaje indicando que el profesor está enseñando

class Curso:
    def __init__(self, nombre, profesor):
        """
        Constructor de la clase Curso.

        Args:
        - nombre (str): El nombre del curso.
        - profesor (Profesor): El objeto Profesor que imparte el curso.
        """
        self.nombre = nombre       # Asigna el nombre del curso al atributo 'nombre'
        self.profesor = profesor   # Asigna el objeto Profesor al atributo 'profesor'

    def detalles(self):
        """Método para obtener los detalles del curso."""
        return f"Curso: {self.nombre}, Profesor: {self.profesor.nombre}"  # Devuelve los detalles del curso, incluyendo el nombre del curso y el nombre del profesor

# Crear una instancia de Profesor
profesor1 = Profesor("Juan")  # Crea una instancia de Profesor con nombre "Juan"

# Crear una instancia de Curso con el profesor previamente creado
curso1 = Curso("Matemáticas", profesor1)  # Crea una instancia de Curso con nombre "Matemáticas" y el profesor "Juan"

# Imprimir los detalles del curso
print(curso1.detalles())             # Salida: Curso: Matemáticas, Profesor: Juan

# Llamar al método enseñar() en la instancia del profesor
print(profesor1.enseñar())          # Salida: Enseñando
