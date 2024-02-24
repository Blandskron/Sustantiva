# Definición de la función calculate_average() que calcula el promedio de una lista de números
def calculate_average(numbers):
    # Verifica si la lista está vacía
    if len(numbers) == 0:
        raise ValueError("La lista está vacía")

    total = 0

    # Itera sobre cada número en la lista
    for num in numbers:
        # Verifica si el elemento no es un número
        if not isinstance(num, (int, float)):
            raise TypeError("La lista contiene elementos no numéricos")
        # Suma cada número al total
        total += num

    # Calcula el promedio dividiendo la suma total entre la cantidad de números
    return total / len(numbers)

# Llamada a la función calculate_average() con una lista de números
response = calculate_average([1, 2, 3, 4, 5])

# Imprime el promedio de la lista de números
print(response)
