class Pueblos:
    def __init__(self, continente):
        self.continente = continente

    class Historicos:
        def __init__(self, nombre):
            self.nombre = nombre

# Ejemplo de uso
pueblos = Pueblos("Europa")
romanos = pueblos.Historicos("Romanos")
vikingos = pueblos.Historicos("Vikingos")
print(f"Continente: {pueblos.continente}")
print(f"Pueblo histórico 1: {romanos.nombre}")
print(f"Pueblo histórico 2: {vikingos.nombre}")
