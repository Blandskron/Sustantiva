class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Departamento: {self.nombre}"


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario:.2f}"


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"Desarrollador: {self.nombre}, Salario: ${self.salario:.2f}, Lenguaje: {self.lenguaje}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, nivel):
        super().__init__(nombre, salario)
        self.nivel = nivel

    def calcular_pago(self):
        return self.salario * 1.10  # Aumento del 10% para gerentes

    def __str__(self):
        return f"Gerente: {self.nombre}, Salario: ${self.salario:.2f}, Nivel: {self.nivel}"


def main():
    departamento_it = Departamento("IT")

    empleado1 = Desarrollador("Juan", 50000, "Python")
    empleado2 = Gerente("María", 60000, "Senior")

    print(departamento_it)
    print(empleado1)
    print(f"Pago de {empleado1.nombre}: ${empleado1.calcular_pago():.2f}")
    print(empleado2)
    print(f"Pago de {empleado2.nombre}: ${empleado2.calcular_pago():.2f}")


if __name__ == "__main__":
    main()
