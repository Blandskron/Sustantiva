class GradoEstudio:
    def __init__(self, nombre, nivel):
        """
        Constructor de la clase GradoEstudio.

        Args:
        - nombre (str): El nombre del grado de estudio.
        - nivel (str): El nivel del grado de estudio.
        """
        self.nombre = nombre
        self.nivel = nivel

    class Detalles:
        def __init__(self, duracion, modalidad):
            """
            Constructor de la clase Detalles.

            Args:
            - duracion (str): La duración del grado de estudio.
            - modalidad (str): La modalidad del grado de estudio.
            """
            self.duracion = duracion
            self.modalidad = modalidad

# Ejemplo de uso
licenciatura = GradoEstudio("Licenciatura en Informática", "Universitario")
licenciatura_detalles = licenciatura.Detalles("4 años", "Presencial")
print(f"Grado de estudio: {licenciatura.nombre}, Nivel: {licenciatura.nivel}")
print(f"Duración: {licenciatura_detalles.duracion}, Modalidad: {licenciatura_detalles.modalidad}")
