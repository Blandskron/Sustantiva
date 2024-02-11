# Definir un diccionario de estudiantes y sus calificaciones
calificaciones = {"Juan": 90, "María": 85, "Pedro": 95, "Ana": 88}

# Iterar sobre el diccionario e imprimir el nombre y la calificación de cada estudiante
print("Calificaciones de los estudiantes:")
for estudiante, calificacion in calificaciones.items():
    print(f"{estudiante}: {calificacion}")
