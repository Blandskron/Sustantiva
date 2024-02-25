class Juego:
    def __init__(self, nombre, desarrollador, plataforma):
        """
        Constructor de la clase Juego.

        Args:
        - nombre (str): El nombre del juego.
        - desarrollador (str): El desarrollador del juego.
        - plataforma (str): Las plataformas en las que está disponible el juego.
        """
        self.nombre = nombre                  # Asigna el nombre del juego al atributo 'nombre'
        self.desarrollador = desarrollador  # Asigna el desarrollador del juego al atributo 'desarrollador'
        self.plataforma = plataforma          # Asigna las plataformas del juego al atributo 'plataforma'

    def detalles(self):
        """Método para imprimir los detalles del juego."""
        print(f"Juego: {self.nombre}")                # Imprime el nombre del juego
        print(f"Desarrollador: {self.desarrollador}")  # Imprime el desarrollador del juego
        print(f"Plataforma: {self.plataforma}")        # Imprime las plataformas del juego

# Crear una instancia de Juego
cyberpunk = Juego("Cyberpunk 2077", "CD Projekt Red", "PC, PS4, Xbox")  # Crea una instancia de Juego con nombre "Cyberpunk 2077", desarrollador "CD Projekt Red" y plataforma "PC, PS4, Xbox"

# Llamar al método 'detalles()' para mostrar los detalles del juego
cyberpunk.detalles()  # Muestra los detalles del juego "Cyberpunk 2077"
