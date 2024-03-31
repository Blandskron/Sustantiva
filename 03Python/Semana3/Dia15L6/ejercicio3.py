# Definir una lista con los nombres de los meses y la cantidad de días que tienen
meses = [
    ("Enero", 31),
    ("Febrero", 28),
    ("Marzo", 31),
    ("Abril", 30),
    ("Mayo", 31),
    ("Junio", 30),
    ("Julio", 31),
    ("Agosto", 31),
    ("Septiembre", 30),
    ("Octubre", 31),
    ("Noviembre", 30),
    ("Diciembre", 31)
]

# Pedir al usuario que ingrese un número de mes
numero_mes = int(input("Ingrese el número del mes (1-12): "))

# Validar que el número de mes esté en el rango correcto
if numero_mes < 1 or numero_mes > 12:
    print("Número de mes inválido.")
else:
    # Obtener el nombre del mes y la cantidad de días correspondiente
    nombre_mes, dias_mes = meses[numero_mes - 1]

    # Mostrar la cantidad de días y el nombre del mes
    print(f"El mes de {nombre_mes} tiene {dias_mes} días.")
