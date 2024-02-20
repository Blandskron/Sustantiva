class GestorTareas:
    def __init__(self):
        self.tareas = []  # Inicializa una lista vacía para almacenar tareas

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)  # Agrega una nueva tarea a la lista
        print("Tarea agregada correctamente.")  # Muestra un mensaje de confirmación

    def mostrar_tareas(self):
        if self.tareas:  # Verifica si hay tareas en la lista
            print("Lista de tareas:")
            for tarea in self.tareas:  # Itera sobre las tareas y las muestra
                print("-", tarea)
        else:
            print("No hay tareas en el gestor.")  # Muestra un mensaje si no hay tareas


class EvaluadorRendimiento:
    def __init__(self):
        self.calificaciones = {}  # Inicializa un diccionario para almacenar calificaciones

    def agregar_calificacion(self, estudiante, calificacion):
        self.calificaciones[estudiante] = calificacion  # Agrega una nueva calificación al diccionario

    def mostrar_calificaciones(self):
        if self.calificaciones:  # Verifica si hay calificaciones en el diccionario
            print("Calificaciones de estudiantes:")
            for estudiante, calificacion in self.calificaciones.items():  # Muestra las calificaciones
                print(f"{estudiante}: {calificacion}")
        else:
            print("No hay calificaciones registradas.")  # Muestra un mensaje si no hay calificaciones


class RegistroContactos:
    def __init__(self):
        self.contactos = {}  # Inicializa un diccionario para almacenar contactos

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono  # Agrega un nuevo contacto al diccionario
        print("Contacto agregado correctamente.")  # Muestra un mensaje de confirmación

    def mostrar_contactos(self):
        if self.contactos:  # Verifica si hay contactos en el diccionario
            print("Lista de contactos:")
            for nombre, telefono in self.contactos.items():  # Muestra los contactos
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("No hay contactos registrados.")  # Muestra un mensaje si no hay contactos


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
gestor_tareas = GestorTareas()  # Instancia del Gestor de Tareas
evaluador_rendimiento = EvaluadorRendimiento()  # Instancia del Evaluador de Rendimiento
registro_contactos = RegistroContactos()  # Instancia del Registro de Contactos
calculadora = CalculadoraAvanzada()  # Instancia de la Calculadora Avanzada

# Menú de opciones para el usuario
while True:
    print("\n----- Menú de opciones -----")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Agregar calificación de estudiante")
    print("4. Mostrar calificaciones")
    print("5. Agregar contacto")
    print("6. Mostrar contactos")
    print("7. Realizar operaciones con la calculadora")
    print("8. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea a agregar: ")
        gestor_tareas.agregar_tarea(tarea)
    elif opcion == "2":
        gestor_tareas.mostrar_tareas()
    elif opcion == "3":
        estudiante = input("Ingrese el nombre del estudiante: ")
        calificacion = int(input("Ingrese la calificación del estudiante: "))
        evaluador_rendimiento.agregar_calificacion(estudiante, calificacion)
    elif opcion == "4":
        evaluador_rendimiento.mostrar_calificaciones()
    elif opcion == "5":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        registro_contactos.agregar_contacto(nombre, telefono)
    elif opcion == "6":
        registro_contactos.mostrar_contactos()
    elif opcion == "7":
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if operacion == "+":
            print("Resultado de la suma:", calculadora.sumar(num1, num2))
        elif operacion == "-":
            print("Resultado de la resta:", calculadora.restar(num1, num2))
        elif operacion == "*":
            print("Resultado de la multiplicación:", calculadora.multiplicar(num1, num2))
        elif operacion == "/":
            print("Resultado de la división:", calculadora.dividir(num1, num2))
        else:
            print("Operación no válida.")
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 8.")
