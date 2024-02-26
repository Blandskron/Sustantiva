class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_salario(self):
        return self.salario

    def aumentar_salario(self, aumento):
        self.salario += aumento


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def obtener_departamento(self):
        return self.departamento

    def asignar_bono(self, bono):
        self.salario += bono


# Creación de instancias de las clases
empleado1 = Empleado("Juan", 30, 3000)
gerente1 = Gerente("Maria", 35, 5000, "Ventas")

# Acceso a los métodos y atributos de las clases
print("Nombre del empleado:", empleado1.obtener_nombre())
print("Edad del empleado:", empleado1.obtener_edad())
print("Salario del empleado:", empleado1.obtener_salario())

print("Nombre del gerente:", gerente1.obtener_nombre())
print("Edad del gerente:", gerente1.obtener_edad())
print("Salario del gerente:", gerente1.obtener_salario())
print("Departamento del gerente:", gerente1.obtener_departamento())

# Aumento de salario para el empleado y asignación de bono para el gerente
empleado1.aumentar_salario(500)
gerente1.asignar_bono(1000)

# Mostrar los salarios actualizados
print("Nuevo salario del empleado:", empleado1.obtener_salario())
print("Nuevo salario del gerente:", gerente1.obtener_salario())
