def combinar_diccionarios(dic1, dic2):
    """
    Esta función combina dos diccionarios.
    
    Parámetros:
    dic1 (dict): El primer diccionario a combinar.
    dic2 (dict): El segundo diccionario a combinar.
    
    Retorna:
    dict: Un diccionario que contiene la combinación de los elementos de los diccionarios de entrada.
    """
    resultado = dic1.copy()  # Creamos una copia del primer diccionario
    resultado.update(dic2)   # Actualizamos el primer diccionario con los elementos del segundo diccionario
    return resultado         # Devolvemos el diccionario combinado

# Ejemplo de uso:
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
print("Diccionario combinado:", combinar_diccionarios(diccionario1, diccionario2))
