class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, salario):
        nuevo_empleado = self.Empleado(nombre, salario)
        self.empleados.append(nuevo_empleado)

    class Empleado:
        def __init__(self, nombre, salario):
            self.nombre = nombre
            self.salario = salario

        def mostrar_info(self):
            print(f"Nombre: {self.nombre}, Salario: ${self.salario}")


# Crear instancia de la clase Empresa y contratar empleados
empresa = Empresa("Empresa ABC")
empresa.contratar_empleado("María", 3000)
empresa.contratar_empleado("Pedro", 3500)

# Mostrar información de los empleados de la empresa
for empleado in empresa.empleados:
    empleado.mostrar_info()
