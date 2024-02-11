# Definición de una función llamada get_student_average que calcula el promedio de calificaciones de los estudiantes.
# Toma un argumento:
# - students: una lista de diccionarios, donde cada diccionario representa un estudiante con su nombre y sus calificaciones.
def get_student_average(students):
    # Inicialización de un diccionario para almacenar la información sobre los promedios de los estudiantes y el promedio de la clase.
    rta = {
        "class_average": 0,  # Promedio de la clase
        "students": []       # Lista de estudiantes con sus promedios
    }
    
    # Iteración sobre cada estudiante en la lista 'students'
    for student in students:
        average = 0  # Inicialización del promedio del estudiante
        grades = student["grades"]  # Obtención de las calificaciones del estudiante actual
        
        # Iteración sobre cada calificación del estudiante
        for grade in grades:
            average += grade  # Suma de las calificaciones para calcular el promedio
        
        # Cálculo del promedio dividiendo la suma de las calificaciones entre la cantidad de calificaciones
        average = average / len(grades)
        
        # Actualización del promedio de la clase sumando el promedio del estudiante actual
        rta["class_average"] += average
        
        # Agregar al diccionario 'students' el nombre del estudiante y su promedio redondeado
        rta["students"].append({
            "name": student["name"],
            "average": round(average, 2)  # Redondea el promedio a dos decimales
        })
    
    # Cálculo final del promedio de la clase dividiendo la suma de los promedios entre la cantidad de estudiantes
    rta["class_average"] = rta["class_average"] / len(students)
    # Redondeo del promedio de la clase a dos decimales
    rta["class_average"] = round(rta["class_average"], 2)
    
    # Devuelve el diccionario 'rta' con los promedios de los estudiantes y el promedio de la clase.
    return rta

# Llama a la función get_student_average con una lista de estudiantes, cada estudiante representado por un diccionario.
# La función devuelve un diccionario con los promedios de los estudiantes y el promedio de la clase.
response = get_student_average([
    {
        "name": "Pedro",
        "grades": [90, 87, 88, 90],
    },
    {
        "name": "Jose",
        "grades": [99, 71, 88, 96],
    },
    {
        "name": "Maria",
        "grades": [92, 81, 80, 96],
    },
])

# Imprime el diccionario con los promedios de los estudiantes y el promedio de la clase.
print(response)
