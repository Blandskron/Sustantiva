class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = []

    def agregar_asignatura(self, nombre, nota):
        nueva_asignatura = self.Asignatura(nombre, nota)
        self.asignaturas.append(nueva_asignatura)

    class Asignatura:
        def __init__(self, nombre, nota):
            self.nombre = nombre
            self.nota = nota

        def obtener_info(self):
            return f"Asignatura: {self.nombre}, Nota: {self.nota}"


# Crear instancia de la clase Estudiante y agregar asignaturas
estudiante = Estudiante("Juan")
estudiante.agregar_asignatura("Matemáticas", 8)
estudiante.agregar_asignatura("Historia", 7)

# Mostrar información de las asignaturas del estudiante
for asignatura in estudiante.asignaturas:
    print(asignatura.obtener_info())
