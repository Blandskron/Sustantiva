class TraductorUniversal:
    def __init__(self, idioma_fuente, idioma_destino):
        self.idioma_fuente = idioma_fuente
        self.idioma_destino = idioma_destino

    def traducir(self, mensaje):
        print(f"Traduciendo del idioma {self.idioma_fuente} al {self.idioma_destino}: {mensaje}")

# Crear una instancia de TraductorUniversal
traductor_marciano = TraductorUniversal("Marciano", "Inglés")
traductor_marciano.traducir("Saludos desde Marte.")
