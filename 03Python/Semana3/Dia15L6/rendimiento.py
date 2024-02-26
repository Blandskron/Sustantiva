# Definición de las asignaturas y las notas del estudiante
notas = {
    "Matemáticas": 0,
    "Ciencias": 0,
    "Historia": 0
}

# Solicitar al usuario que ingrese las notas para cada asignatura
for asignatura in notas:
    nota = float(input(f"Ingrese la nota para {asignatura}: "))
    notas[asignatura] = nota

# Calcular el promedio de las notas
promedio = sum(notas.values()) / len(notas)

# Mostrar el rendimiento del estudiante
print("\nRendimiento del estudiante:")
for asignatura, nota in notas.items():
    if nota >= 6:
        resultado = "Aprobado"
    else:
        resultado = "Reprobado"
    print(f"{asignatura}: {nota} - {resultado}")

print(f"\nPromedio: {promedio}")
