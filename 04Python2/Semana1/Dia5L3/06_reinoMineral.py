class ReinoMineral:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # Nombre del mineral
        self.tipo = tipo      # Tipo de formación del mineral (geológicos, químicos, etc.)

    def formacion(self):
        # Método para describir cómo se formó el mineral
        print(f"El mineral {self.nombre} se formó por procesos {self.tipo}.")

# Creación de una instancia de la clase ReinoMineral
diamante = ReinoMineral("Diamante", "geológicos")

# Llamada al método formacion() para describir cómo se formó el diamante
diamante.formacion()
