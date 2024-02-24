class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, matricula):
        super().__init__(nombre, edad, genero)
        self.matricula = matricula
        self.cursos = []

    def inscribir_curso(self, curso):
        self.cursos.append(curso)

    def pagar_matricula(self, cantidad):
        # Método para pagar matrícula
        pass

    def ver_cursos(self):
        return self.cursos


class Profesor(Persona):
    def __init__(self, nombre, edad, genero, especialidad):
        super().__init__(nombre, edad, genero)
        self.especialidad = especialidad
        self.cursos_asignados = []

    def asignar_curso(self, curso):
        self.cursos_asignados.append(curso)

    def calificar_estudiante(self, estudiante, nota):
        # Método para calificar a un estudiante
        pass

    def ver_cursos_asignados(self):
        return self.cursos_asignados


class Curso:
    def __init__(self, nombre, codigo, horario, aula):
        self.nombre = nombre
        self.codigo = codigo
        self.horario = horario
        self.aula = aula

    def obtener_nombre(self):
        return self.nombre

    def obtener_codigo(self):
        return self.codigo

    def obtener_horario(self):
        return self.horario


class Asignatura:
    def __init__(self, nombre, codigo, horas_semanales):
        self.nombre = nombre
        self.codigo = codigo
        self.horas_semanales = horas_semanales

    def obtener_nombre(self):
        return self.nombre

    def obtener_codigo(self):
        return self.codigo

    def obtener_horas_semanales(self):
        return self.horas_semanales


class Aula:
    def __init__(self, numero, capacidad, edificio):
        self.numero = numero
        self.capacidad = capacidad
        self.edificio = edificio

    def obtener_numero(self):
        return self.numero

    def obtener_capacidad(self):
        return self.capacidad

    def obtener_edificio(self):
        return self.edificio


class Horario:
    def __init__(self, dia_semana, hora_inicio, hora_fin):
        self.dia_semana = dia_semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def obtener_dia_semana(self):
        return self.dia_semana

    def obtener_hora_inicio(self):
        return self.hora_inicio

    def obtener_hora_fin(self):
        return self.hora_fin


# Ejemplo de uso
# Crear instancias de las clases
estudiante1 = Estudiante("Juan", 20, "Masculino", "2022001")
profesor1 = Profesor("María", 35, "Femenino", "Matemáticas")
curso1 = Curso("Matemáticas Avanzadas", "MAT101", "Lunes 8:00-10:00", "Aula 101")
asignatura1 = Asignatura("Álgebra Lineal", "ALG102", 4)
aula1 = Aula("Aula 101", 30, "Edificio A")
horario1 = Horario("Lunes", "8:00", "10:00")

# Interacciones
estudiante1.inscribir_curso(curso1)
profesor1.asignar_curso(curso1)

# Mostrar información
print("Nombre del estudiante:", estudiante1.obtener_nombre())
print("Cursos inscritos:", [curso.obtener_nombre() for curso in estudiante1.ver_cursos()])
print("Nombre del profesor:", profesor1.obtener_nombre())
print("Cursos asignados:", [curso.obtener_nombre() for curso in profesor1.ver_cursos_asignados()])
