class Idiomas:
    def __init__(self, familia):
        """
        Constructor de la clase Idiomas.

        Args:
        - familia (str): La familia lingüística a la que pertenecen los idiomas.
        """
        self.familia = familia

    class Lenguas:
        def __init__(self, nombre):
            """
            Constructor de la clase Lenguas.

            Args:
            - nombre (str): El nombre del idioma.
            """
            self.nombre = nombre

# Ejemplo de uso
idiomas = Idiomas("Indoeuropea")
espanol = idiomas.Lenguas("Español")
ingles = idiomas.Lenguas("Inglés")
print(f"Familia de idiomas: {idiomas.familia}")
print(f"Idioma 1: {espanol.nombre}")
print(f"Idioma 2: {ingles.nombre}")
