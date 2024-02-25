class TiposAnimales:
    def __init__(self, tipo):
        self.tipo = tipo

    def clasificacion(self):
        print(f"Los animales de tipo {self.tipo} se clasifican según diferentes criterios.")


# Uso de la clase
mamiferos = TiposAnimales("mamíferos")
mamiferos.clasificacion()
