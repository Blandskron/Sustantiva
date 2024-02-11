def combinar_diccionarios(dic1, dic2):
    """Esta función combina dos diccionarios."""
    resultado = dic1.copy()
    resultado.update(dic2)
    return resultado

# Ejemplo de uso:
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
print("Diccionario combinado:", combinar_diccionarios(diccionario1, diccionario2))
