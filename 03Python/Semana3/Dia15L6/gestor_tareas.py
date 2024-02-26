# Función para agregar una nueva tarea a la lista de tareas
def agregar_tarea(tarea, lista_tareas):
    lista_tareas.append(tarea)
    print("Tarea agregada exitosamente.")

# Función para mostrar todas las tareas en la lista
def mostrar_tareas(lista_tareas):
    if lista_tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas, start=1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

# Función para marcar una tarea como completada
def completar_tarea(numero_tarea, lista_tareas):
    if 1 <= numero_tarea <= len(lista_tareas):
        tarea_completada = lista_tareas.pop(numero_tarea - 1)
        print(f"Tarea '{tarea_completada}' completada.")
    else:
        print("Número de tarea inválido.")

# Función para guardar las tareas en un archivo de texto
def guardar_tareas(nombre_archivo, lista_tareas):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for tarea in lista_tareas:
                archivo.write(tarea + '\n')
        print("Tareas guardadas en el archivo correctamente.")
    except IOError:
        print("Error al guardar las tareas en el archivo.")

# Lista para almacenar las tareas
tareas = []

# Menú principal
while True:
    print("\n--- GESTIÓN DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Guardar tareas")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == '1':
        nueva_tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(nueva_tarea, tareas)
    elif opcion == '2':
        mostrar_tareas(tareas)
    elif opcion == '3':
        if tareas:
            mostrar_tareas(tareas)
            num_tarea_completada = int(input("Ingrese el número de la tarea completada: "))
            completar_tarea(num_tarea_completada, tareas)
        else:
            print("No hay tareas para completar.")
    elif opcion == '4':
        nombre_archivo = input("Ingrese el nombre del archivo para guardar las tareas: ")
        guardar_tareas(nombre_archivo, tareas)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
