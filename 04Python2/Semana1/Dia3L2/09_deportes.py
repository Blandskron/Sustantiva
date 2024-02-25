class Deporte:
    def __init__(self, nombre, tipo):
        """
        Constructor de la clase Deporte.

        Args:
        - nombre (str): El nombre del deporte.
        - tipo (str): El tipo de deporte.
        """
        self.nombre = nombre
        self.tipo = tipo

    class Reglas:
        def __init__(self, num_jugadores, campo):
            """
            Constructor de la clase Reglas.

            Args:
            - num_jugadores (str): El número de jugadores requerido.
            - campo (str): El tipo de campo requerido.
            """
            self.num_jugadores = num_jugadores
            self.campo = campo

# Ejemplo de uso
futbol = Deporte("Fútbol", "Colectivo")
futbol_reglas = futbol.Reglas("11 jugadores", "Campo de hierba")
print(f"Deporte: {futbol.nombre}, Tipo: {futbol.tipo}")
print(f"Número de jugadores: {futbol_reglas.num_jugadores}, Campo: {futbol_reglas.campo}")
