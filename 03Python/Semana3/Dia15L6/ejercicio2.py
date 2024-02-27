# Pedir al usuario que ingrese las 5 notas
print("Ingrese las 5 notas del alumno:")
notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    while nota < 0 or nota > 10:  # Validar que la nota esté entre 0 y 10
        print("La nota debe estar entre 0 y 10")
        nota = float(input(f"Ingrese la nota {i + 1} nuevamente: "))
    notas.append(nota)

# Ordenar las notas de mayor a menor
notas.sort(reverse=True)

# Mostrar las notas ordenadas
print("Notas del alumno de mayor a menor:")
for nota in notas:
    print(nota)
