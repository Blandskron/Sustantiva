# Pedir al usuario la cantidad de notas a ingresar
cantidad_notas = int(input("Ingrese la cantidad de notas a ingresar: "))

# Inicializar la suma de las notas
suma_notas = 0

# Pedir al usuario que ingrese las notas una por una
for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma_notas += nota  # Sumar la nota ingresada a la suma total

# Calcular el promedio de las notas
if cantidad_notas > 0:
    promedio = suma_notas / cantidad_notas
else:
    promedio = 0

# Mostrar la cantidad de notas ingresadas y el promedio
print(f"Se ingresaron {cantidad_notas} notas.")
print(f"El promedio de las notas ingresadas es: {promedio}")
