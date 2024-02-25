class LenguajeProgramacion:
    def __init__(self, nombre):
        """
        Constructor de la clase LenguajeProgramacion.

        Args:
        - nombre (str): El nombre del lenguaje de programación.
        """
        self.nombre = nombre

    class Caracteristicas:
        def __init__(self, tipo, popularidad):
            """
            Constructor de la clase Caracteristicas.

            Args:
            - tipo (str): El tipo de lenguaje de programación.
            - popularidad (str): El nivel de popularidad del lenguaje.
            """
            self.tipo = tipo
            self.popularidad = popularidad

# Ejemplo de uso
lenguaje = LenguajeProgramacion("Python")
caracteristicas = lenguaje.Caracteristicas("Interpretado", "Alta")
print(f"Lenguaje de Programación: {lenguaje.nombre}")
print(f"Tipo: {caracteristicas.tipo}, Popularidad: {caracteristicas.popularidad}")
