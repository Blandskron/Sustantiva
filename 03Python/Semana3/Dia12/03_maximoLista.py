def obtener_maximo(lista):
    """
    Esta función recibe una lista de números y devuelve el máximo.
    
    Parámetros:
    lista (list): Una lista de números enteros o flotantes.
    
    Retorna:
    int o float: El número máximo de la lista. Si la lista está vacía, retorna None.
    """
    if not lista:
        return None  # Devuelve None si la lista está vacía
    
    maximo = lista[0]  # Asigna el primer elemento de la lista como máximo inicialmente
    
    # Itera sobre cada elemento de la lista para encontrar el máximo
    for num in lista:
        if num > maximo:
            maximo = num  # Actualiza el máximo si encuentra un número mayor
    
    return maximo

# Ejemplo de uso:
numeros = [3, 8, 1, 6, 4]
print("El máximo de la lista es:", obtener_maximo(numeros))
