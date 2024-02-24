class Energia:
    def __init__(self, tipo):
        self.tipo = tipo

    class Materia:
        def __init__(self, nombre, estado):
            self.nombre = nombre
            self.estado = estado

# Ejemplo de uso
energia = Energia("Eléctrica")
materia = energia.Materia("Cobre", "Sólido")
print(f"Tipo de energía: {energia.tipo}")
print(f"Materia: {materia.nombre}, Estado: {materia.estado}")
