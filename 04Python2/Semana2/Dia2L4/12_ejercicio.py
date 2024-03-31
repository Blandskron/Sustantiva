class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estoy en {self.grado} grado.")

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy profesor de {self.especialidad}.")

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Estudiantes inscritos en el curso de {self.nombre}:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre}")

# Instanciar objetos
profesor_john = Profesor("John", 35, "Matemáticas")
estudiante_maria = Estudiante("Maria", 15, 9)
estudiante_jose = Estudiante("Jose", 14, 8)

curso_matematicas = Curso("Matemáticas Avanzadas", profesor_john)

# Agregar estudiantes al curso
curso_matematicas.agregar_estudiante(estudiante_maria)
curso_matematicas.agregar_estudiante(estudiante_jose)

# Mostrar estudiantes del curso
curso_matematicas.mostrar_estudiantes()

# Interacción entre objetos
profesor_john.presentarse()
estudiante_maria.presentarse()
