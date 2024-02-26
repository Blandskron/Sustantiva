# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad


# Definición de la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def obtener_curso(self):
        return self.curso


# Definición de la clase Profesor que hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def obtener_especialidad(self):
        return self.especialidad


# Creación de instancias de las clases
estudiante1 = Estudiante("Juan", 20, "Python")
profesor1 = Profesor("María", 35, "Informática")

# Acceso a los métodos y atributos de las clases
print("Nombre del estudiante:", estudiante1.obtener_nombre())
print("Edad del estudiante:", estudiante1.obtener_edad())
print("Curso del estudiante:", estudiante1.obtener_curso())

print("Nombre del profesor:", profesor1.obtener_nombre())
print("Edad del profesor:", profesor1.obtener_edad())
print("Especialidad del profesor:", profesor1.obtener_especialidad())
