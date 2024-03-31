class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        else:
            total_calificaciones = sum(self.calificaciones)
            return total_calificaciones / len(self.calificaciones)


def main():
    # Crear estudiantes
    estudiante1 = Estudiante("Juan", 20)
    estudiante2 = Estudiante("María", 22)
    estudiante3 = Estudiante("Pedro", 21)

    # Agregar calificaciones
    estudiante1.agregar_calificacion(85)
    estudiante1.agregar_calificacion(90)
    estudiante1.agregar_calificacion(78)

    estudiante2.agregar_calificacion(92)
    estudiante2.agregar_calificacion(88)
    estudiante2.agregar_calificacion(91)

    estudiante3.agregar_calificacion(75)
    estudiante3.agregar_calificacion(80)
    estudiante3.agregar_calificacion(85)

    # Calcular promedio
    print(f"El promedio de {estudiante1.nombre} es: {estudiante1.calcular_promedio()}")
    print(f"El promedio de {estudiante2.nombre} es: {estudiante2.calcular_promedio()}")
    print(f"El promedio de {estudiante3.nombre} es: {estudiante3.calcular_promedio()}")


if __name__ == "__main__":
    main()
