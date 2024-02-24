class Deporte:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    class Reglas:
        def __init__(self, num_jugadores, campo):
            self.num_jugadores = num_jugadores
            self.campo = campo

# Ejemplo de uso
futbol = Deporte("Fútbol", "Colectivo")
futbol_reglas = futbol.Reglas("11 jugadores", "Campo de hierba")
print(f"Deporte: {futbol.nombre}, Tipo: {futbol.tipo}")
print(f"Número de jugadores: {futbol_reglas.num_jugadores}, Campo: {futbol_reglas.campo}")
