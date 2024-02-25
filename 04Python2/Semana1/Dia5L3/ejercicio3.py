class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo


class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def asignar_asignatura(self, asignatura):
        print(f"El profesor {self.nombre} imparte la asignatura {asignatura.nombre}")


class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso


class Curso:
    def __init__(self, año_academico):
        self.año_academico = año_academico
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)


# Creación de instancias
asignatura1 = Asignatura("Matemáticas", "MAT101")
asignatura2 = Asignatura("Ciencias", "CIE102")

profesor1 = Profesor("Juan Pérez", "Matemáticas")
profesor2 = Profesor("María González", "Ciencias")

curso1 = Curso(2024)
curso1.agregar_asignatura(asignatura1)
curso1.agregar_asignatura(asignatura2)

alumno1 = Alumno("Pedro", 15, curso1)
alumno2 = Alumno("Ana", 16, curso1)

# Asignación de profesores a asignaturas
profesor1.asignar_asignatura(asignatura1)
profesor2.asignar_asignatura(asignatura2)
