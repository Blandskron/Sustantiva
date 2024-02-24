class MedioTransporte:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    class Caracteristicas:
        def __init__(self, velocidad_maxima, capacidad):
            self.velocidad_maxima = velocidad_maxima
            self.capacidad = capacidad

# Ejemplo de uso
bicicleta = MedioTransporte("Bicicleta", "Terrestre")
bicicleta_caract = bicicleta.Caracteristicas("30 km/h", "1 persona")
print(f"Medio de transporte: {bicicleta.nombre}, Tipo: {bicicleta.tipo}")
print(f"Velocidad máxima: {bicicleta_caract.velocidad_maxima}, Capacidad: {bicicleta_caract.capacidad}")
