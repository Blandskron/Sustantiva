class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando en la carrera de {self.carrera}.")


# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("Ana", 20, "Ingeniería Civil")
estudiante2 = Estudiante("Pedro", 22, "Medicina")

# Acceder a los atributos y métodos de las instancias
print(estudiante1.edad)   # Imprime: 20
print(estudiante2.carrera)  # Imprime: Medicina
estudiante1.estudiar()    # Imprime: Ana está estudiando en la carrera de Ingeniería Civil.
