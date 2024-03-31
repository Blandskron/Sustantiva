class Estrella:
    def __init__(self, nombre, tipo):
        """
        Constructor de la clase Estrella.

        Args:
        - nombre (str): El nombre de la estrella.
        - tipo (str): El tipo de la estrella.
        """
        self.nombre = nombre
        self.tipo = tipo

    class Planeta:
        def __init__(self, nombre, masa, distancia):
            """
            Constructor de la clase Planeta.

            Args:
            - nombre (str): El nombre del planeta.
            - masa (str): La masa del planeta.
            - distancia (str): La distancia del planeta a la estrella.
            """
            self.nombre = nombre
            self.masa = masa
            self.distancia = distancia

# Ejemplo de uso
sol = Estrella("Sol", "Enana amarilla")
tierra = sol.Planeta("Tierra", "5.972 × 10^24 kg", "149.6 millones km")
print(f"Estrella: {sol.nombre}, Tipo: {sol.tipo}")
print(f"Planeta: {tierra.nombre}, Masa: {tierra.masa}, Distancia: {tierra.distancia}")
