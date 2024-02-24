# Definición de la función my_map() que implementa una versión simplificada de la función map()
def my_map(list, func):
    # Inicializa una nueva lista vacía para almacenar los resultados
    new_list = []
    # Itera sobre cada elemento en la lista dada
    for item in list:
        # Aplica la función func a cada elemento y agrega el resultado a la nueva lista
        new_list.append(func(item))
    # Retorna la nueva lista que contiene los resultados de aplicar la función a cada elemento
    return new_list

# Llamada a la función my_map() con una lista y una función lambda
response = my_map([1, 2, 3, 4], lambda num: num * 2)

# Imprime la lista resultante después de aplicar la función lambda a cada elemento
print(response)
