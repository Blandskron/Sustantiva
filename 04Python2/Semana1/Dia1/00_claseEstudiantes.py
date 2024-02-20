class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso}")

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Ana", 20, "Matemáticas")
estudiante1.mostrar_info()
