def obtener_maximo(lista):
    """Esta función recibe una lista de números y devuelve el máximo."""
    if not lista:
        return None  # Devuelve None si la lista está vacía
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

# Ejemplo de uso:
numeros = [3, 8, 1, 6, 4]
print("El máximo de la lista es:", obtener_maximo(numeros))
