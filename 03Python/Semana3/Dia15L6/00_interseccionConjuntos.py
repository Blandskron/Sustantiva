# Definición de la función find_set_intersection() que encuentra la intersección de un conjunto de conjuntos
def find_set_intersection(sets):
    # Verifica si la lista de conjuntos está vacía
    if len(sets) == 0:
        return set()  # Retorna un conjunto vacío si no hay conjuntos para encontrar la intersección
    
    intersection = sets[0]  # Inicializa el conjunto de intersección con el primer conjunto de la lista
    
    # Itera sobre los conjuntos restantes y encuentra la intersección con el conjunto de intersección actual
    for item in sets[1:]:
        intersection = intersection.intersection(item)
    
    return intersection  # Retorna el conjunto de intersección encontrado

# Llamada a la función find_set_intersection() con una lista de conjuntos
response = find_set_intersection([
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
])

# Imprime el resultado de la intersección de los conjuntos
print(response)
