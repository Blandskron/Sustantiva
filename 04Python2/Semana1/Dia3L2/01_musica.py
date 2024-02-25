class Musica:
    def __init__(self, nombre):
        """
        Constructor de la clase Musica.

        Args:
        - nombre (str): El nombre de la música.
        """
        self.nombre = nombre

    class Estilos:
        def __init__(self, estilo):
            """
            Constructor de la clase Estilos.

            Args:
            - estilo (str): El estilo musical.
            """
            self.estilo = estilo

# Ejemplo de uso
musica = Musica("Música")
rock = musica.Estilos("Rock")
jazz = musica.Estilos("Jazz")
print(f"Nombre de la música: {musica.nombre}")
print(f"Estilo 1: {rock.estilo}")
print(f"Estilo 2: {jazz.estilo}")
