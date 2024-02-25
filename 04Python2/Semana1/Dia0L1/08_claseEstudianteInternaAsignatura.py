class Estudiante:
    def __init__(self, nombre):
        """
        Constructor de la clase Estudiante.

        Args:
        - nombre (str): El nombre del estudiante.
        """
        self.nombre = nombre    # Asigna el nombre del estudiante al atributo 'nombre'
        self.asignaturas = []   # Inicializa una lista vacía para almacenar las asignaturas del estudiante

    def agregar_asignatura(self, nombre, nota):
        """
        Método para agregar una nueva asignatura al estudiante.

        Args:
        - nombre (str): El nombre de la asignatura.
        - nota (float): La nota del estudiante en la asignatura.
        """
        nueva_asignatura = self.Asignatura(nombre, nota)  # Crea una nueva instancia de la clase Asignatura
        self.asignaturas.append(nueva_asignatura)         # Agrega la nueva asignatura a la lista de asignaturas del estudiante

    class Asignatura:
        def __init__(self, nombre, nota):
            """
            Constructor de la clase Asignatura.

            Args:
            - nombre (str): El nombre de la asignatura.
            - nota (float): La nota del estudiante en la asignatura.
            """
            self.nombre = nombre    # Asigna el nombre de la asignatura al atributo 'nombre'
            self.nota = nota        # Asigna la nota del estudiante en la asignatura al atributo 'nota'

        def obtener_info(self):
            """
            Método para obtener la información de la asignatura.

            Returns:
            - str: Una cadena que contiene el nombre de la asignatura y la nota del estudiante en ella.
            """
            return f"Asignatura: {self.nombre}, Nota: {self.nota}"


# Crear instancia de la clase Estudiante y agregar asignaturas
estudiante = Estudiante("Juan")                         # Crea una instancia de Estudiante con nombre "Juan"
estudiante.agregar_asignatura("Matemáticas", 8)         # Agrega la asignatura Matemáticas con nota 8 al estudiante
estudiante.agregar_asignatura("Historia", 7)            # Agrega la asignatura Historia con nota 7 al estudiante

# Mostrar información de las asignaturas del estudiante
for asignatura in estudiante.asignaturas:               # Itera sobre las asignaturas del estudiante
    print(asignatura.obtener_info())                     # Muestra la información de cada asignatura
