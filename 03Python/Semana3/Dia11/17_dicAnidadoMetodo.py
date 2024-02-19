# Creamos un diccionario llamado 'estudiantes' donde las claves son los nombres de los estudiantes
# y los valores son diccionarios que contienen las calificaciones de cada estudiante en diferentes materias.
estudiantes = {
    'Juan': {'matemáticas': 90, 'historia': 85, 'ciencias': 95},
    'María': {'matemáticas': 88, 'historia': 92, 'ciencias': 85},
    'Carlos': {'matemáticas': 95, 'historia': 78, 'ciencias': 80}
}

# Acceder a las calificaciones de un estudiante específico (María en este caso)
print("Las calificaciones de María son:", estudiantes['María'])

# Obtener la calificación de matemáticas de Juan
print("La calificación de Juan en matemáticas es:", estudiantes['Juan']['matemáticas'])

# Agregar una nueva calificación para un estudiante (literatura para Juan)
estudiantes['Juan']['literatura'] = 75
print("Las calificaciones actualizadas de Juan son:", estudiantes['Juan'])

# Eliminar la entrada de literatura para Juan
del estudiantes['Juan']['literatura']
print("Después de eliminar la calificación de literatura para Juan:", estudiantes['Juan'])
