class MedioTransporte:
    def __init__(self, nombre, tipo):
        """
        Constructor de la clase MedioTransporte.

        Args:
        - nombre (str): El nombre del medio de transporte.
        - tipo (str): El tipo de medio de transporte.
        """
        self.nombre = nombre
        self.tipo = tipo

    class Caracteristicas:
        def __init__(self, velocidad_maxima, capacidad):
            """
            Constructor de la clase Caracteristicas.

            Args:
            - velocidad_maxima (str): La velocidad máxima del medio de transporte.
            - capacidad (str): La capacidad del medio de transporte.
            """
            self.velocidad_maxima = velocidad_maxima
            self.capacidad = capacidad

# Ejemplo de uso
bicicleta = MedioTransporte("Bicicleta", "Terrestre")
bicicleta_caract = bicicleta.Caracteristicas("30 km/h", "1 persona")
print(f"Medio de transporte: {bicicleta.nombre}, Tipo: {bicicleta.tipo}")
print(f"Velocidad máxima: {bicicleta_caract.velocidad_maxima}, Capacidad: {bicicleta_caract.capacidad}")
