class TiposAnimales:
    def __init__(self, tipo):
        self.tipo = tipo  # Define el tipo de animales

    def clasificacion(self):
        # Método para imprimir la clasificación de los animales según su tipo
        print(f"Los animales de tipo {self.tipo} se clasifican según diferentes criterios.")

# Creación de una instancia de la clase TiposAnimales para mamíferos
mamiferos = TiposAnimales("mamíferos")

# Llamada al método clasificacion() para imprimir la clasificación de los mamíferos
mamiferos.clasificacion()
