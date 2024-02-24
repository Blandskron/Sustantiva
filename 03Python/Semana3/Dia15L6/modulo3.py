# Definir la clase para la gestión de tareas
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada correctamente.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for tarea in self.tareas:
                print("-", tarea)
        else:
            print("No hay tareas en el gestor.")

# Definir la clase para evaluar rendimiento de estudiantes
class EvaluadorRendimiento:
    def __init__(self):
        self.calificaciones = {}

    def agregar_calificacion(self, estudiante, calificacion):
        self.calificaciones[estudiante] = calificacion

    def mostrar_calificaciones(self):
        if self.calificaciones:
            print("Calificaciones de estudiantes:")
            for estudiante, calificacion in self.calificaciones.items():
                print(f"{estudiante}: {calificacion}")
        else:
            print("No hay calificaciones registradas.")

# Definir la clase para el registro de contactos
class RegistroContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("No hay contactos registrados.")

# Definir la clase para la calculadora avanzada
class CalculadoraAvanzada:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

# Instanciar las clases
gestor_tareas = GestorTareas()
evaluador_rendimiento = EvaluadorRendimiento()
registro_contactos = RegistroContactos()
calculadora = CalculadoraAvanzada()

# Agregar tareas al gestor de tareas
gestor_tareas.agregar_tarea("Hacer la compra")
gestor_tareas.agregar_tarea("Estudiar para el examen")

# Mostrar tareas
gestor_tareas.mostrar_tareas()

# Agregar calificaciones de estudiantes
evaluador_rendimiento.agregar_calificacion("Juan", 85)
evaluador_rendimiento.agregar_calificacion("María", 92)

# Mostrar calificaciones de estudiantes
evaluador_rendimiento.mostrar_calificaciones()

# Agregar contactos al registro de contactos
registro_contactos.agregar_contacto("Juan", "123456789")
registro_contactos.agregar_contacto("María", "987654321")

# Mostrar contactos
registro_contactos.mostrar_contactos()

# Realizar operaciones con la calculadora avanzada
print("Resultado de la suma:", calculadora.sumar(10, 5))
print("Resultado de la resta:", calculadora.restar(10, 5))
print("Resultado de la multiplicación:", calculadora.multiplicar(10, 5))
print("Resultado de la división:", calculadora.dividir(10, 5))
