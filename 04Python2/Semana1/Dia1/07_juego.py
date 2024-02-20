class Juego:
    def __init__(self, nombre, desarrollador, plataforma):
        self.nombre = nombre
        self.desarrollador = desarrollador
        self.plataforma = plataforma

    def detalles(self):
        print(f"Juego: {self.nombre}")
        print(f"Desarrollador: {self.desarrollador}")
        print(f"Plataforma: {self.plataforma}")

# Crear una instancia de Juego
cyberpunk = Juego("Cyberpunk 2077", "CD Projekt Red", "PC, PS4, Xbox")
cyberpunk.detalles()
