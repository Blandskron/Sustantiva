class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def enseniar(self):
        return "Enseñando"

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def detalles(self):
        return f"Curso: {self.nombre}, Profesor: {self.profesor.nombre}"


profesor1 = Profesor("Juan")
curso1 = Curso("Matemáticas", profesor1)

print(curso1.detalles())  # Salida: Curso: Matemáticas, Profesor: Juan
print(profesor1.enseniar())  # Salida: Enseñando
