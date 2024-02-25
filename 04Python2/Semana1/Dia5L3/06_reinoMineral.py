class ReinoMineral:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def formacion(self):
        print(f"El mineral {self.nombre} se formó por procesos {self.tipo}.")


# Uso de la clase
diamante = ReinoMineral("Diamante", "geológicos")
diamante.formacion()
