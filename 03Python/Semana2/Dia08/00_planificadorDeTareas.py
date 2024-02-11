# Definición de un diccionario que contiene tareas y su tiempo estimado en minutos
tareas = {"Hacer ejercicio": 30, "Leer": 45, "Cocinar": 60}

# Iteración sobre el diccionario 'tareas', desempaquetando las claves (tarea) y valores (tiempo)
for tarea, tiempo in tareas.items():
    # Imprime un mensaje indicando la tarea y su tiempo estimado
    print(f"Comienza a hacer '{tarea}' por {tiempo} minutos.")
    
    # Bucle interno que cuenta hacia atrás desde el tiempo estimado hasta 0, de 5 en 5 minutos
    for minuto in range(tiempo, 0, -5):
        # Imprime un mensaje indicando cuántos minutos quedan para terminar la tarea
        print(f"Te quedan {minuto} minutos para terminar.")
    
    # Imprime un mensaje indicando que es tiempo para la siguiente tarea
    print(f"¡Tiempo para la siguiente tarea!\n")
