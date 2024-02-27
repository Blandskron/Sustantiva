def createTaskPlanner():
    tasks = []  # Inicializa una lista vacía para almacenar las tareas

    # Método para agregar una tarea a la lista
    def addTask(task):
        task['completed'] = False  # Agrega un campo 'completed' a la tarea con valor False
        tasks.append(task)  # Agrega la tarea a la lista de tareas

    # Método para eliminar una tarea de la lista
    def removeTask(value):
        if isinstance(value, int):  # Si se pasa un ID como argumento
            tasks[:] = [task for task in tasks if task['id'] != value]  # Elimina la tarea con el ID dado de la lista
        elif isinstance(value, str):  # Si se pasa un nombre como argumento
            tasks[:] = [task for task in tasks if task['name'] != value]  # Elimina la tarea con el nombre dado de la lista

    # Método para obtener una copia de la lista de tareas
    def getTasks():
        return tasks[:]  # Devuelve una copia de la lista de tareas para evitar la modificación directa

    # Método para obtener las tareas pendientes (no completadas)
    def getPendingTasks():
        return [task for task in tasks if not task['completed']]  # Filtra las tareas no completadas

    # Método para obtener las tareas completadas
    def getCompletedTasks():
        return [task for task in tasks if task['completed']]  # Filtra las tareas completadas

    # Método para marcar una tarea como completada
    def markTaskAsCompleted(value):
        if isinstance(value, int):  # Si se pasa un ID como argumento
            for task in tasks:
                if task['id'] == value:
                    task['completed'] = True  # Marca la tarea como completada si encuentra el ID
                    break
        elif isinstance(value, str):  # Si se pasa un nombre como argumento
            for task in tasks:
                if task['name'] == value:
                    task['completed'] = True  # Marca la tarea como completada si encuentra el nombre
                    break

    # Método para obtener las tareas ordenadas por prioridad
    def getSortedTasksByPriority():
        return sorted(tasks, key=lambda task: task['priority'])  # Ordena las tareas por prioridad

    # Método para filtrar las tareas por etiqueta
    def filterTasksByTag(tag):
        return [task for task in tasks if tag in task['tags']]  # Filtra las tareas que contienen la etiqueta dada

    # Método para actualizar una tarea con nuevos datos
    def updateTask(taskId, updates):
        for task in tasks:
            if task['id'] == taskId:  # Busca la tarea por ID
                task.update(updates)  # Actualiza los campos de la tarea con los nuevos datos
                break

    # Devuelve un diccionario que contiene todos los métodos definidos anteriormente
    return {
        'addTask': addTask,
        'removeTask': removeTask,
        'getTasks': getTasks,
        'getPendingTasks': getPendingTasks,
        'getCompletedTasks': getCompletedTasks,
        'markTaskAsCompleted': markTaskAsCompleted,
        'getSortedTasksByPriority': getSortedTasksByPriority,
        'filterTasksByTag': filterTasksByTag,
        'updateTask': updateTask,
    }

# Crea una instancia de TaskPlanner
taskPlanner = createTaskPlanner()
