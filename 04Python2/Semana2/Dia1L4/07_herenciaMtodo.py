class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años."


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def descripcion(self):
        return f"{super().descripcion()} Está en {self.grado} grado."


estudiante = Estudiante("Ronald", 12, 6)
print(estudiante.descripcion())  # Salida: Ronald tiene 12 años. Está en 6 grado.
