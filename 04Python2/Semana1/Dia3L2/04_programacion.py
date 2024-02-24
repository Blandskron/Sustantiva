class LenguajeProgramacion:
    def __init__(self, nombre):
        self.nombre = nombre

    class Caracteristicas:
        def __init__(self, tipo, popularidad):
            self.tipo = tipo
            self.popularidad = popularidad

# Ejemplo de uso
lenguaje = LenguajeProgramacion("Python")
caracteristicas = lenguaje.Caracteristicas("Interpretado", "Alta")
print(f"Lenguaje de Programación: {lenguaje.nombre}")
print(f"Tipo: {caracteristicas.tipo}, Popularidad: {caracteristicas.popularidad}")
