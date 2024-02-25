class Energia:
    def __init__(self, tipo):
        """
        Constructor de la clase Energia.

        Args:
        - tipo (str): El tipo de energía.
        """
        self.tipo = tipo

    class Materia:
        def __init__(self, nombre, estado):
            """
            Constructor de la clase Materia.

            Args:
            - nombre (str): El nombre de la materia.
            - estado (str): El estado de la materia.
            """
            self.nombre = nombre
            self.estado = estado

# Ejemplo de uso
energia = Energia("Eléctrica")
materia = energia.Materia("Cobre", "Sólido")
print(f"Tipo de energía: {energia.tipo}")
print(f"Materia: {materia.nombre}, Estado: {materia.estado}")
