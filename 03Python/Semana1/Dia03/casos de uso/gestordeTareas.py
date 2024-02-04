# Definición de la clase Task para representar una tarea
class Task:
    def __init__(self, description, priority):
        self.description = description  # Descripción de la tarea
        self.priority = priority        # Prioridad de la tarea

# Definición de la función principal para la gestión de tareas
def main():
    tasks = []  # Lista para almacenar las tareas
    
    while True:
        print("\nBienvenido al Gestor de Tareas")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            # Solicitar al usuario ingresar los detalles de la tarea
            description = input("Ingrese la descripción de la tarea: ")
            priority = input("Ingrese la prioridad de la tarea (alta, media, baja): ")

            # Crear un objeto Task con los detalles ingresados
            task = Task(description, priority)
            
            # Agregar la tarea a la lista de tareas
            tasks.append(task)
            print("Tarea agregada exitosamente!")

        elif choice == '2':
            # Mostrar todas las tareas almacenadas en la lista
            if tasks:
                print("\nLista de Tareas:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. Descripción: {task.description} - Prioridad: {task.priority}")
            else:
                print("No hay tareas almacenadas.")
        
        elif choice == '3':
            print("¡Gracias por usar el Gestor de Tareas!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
