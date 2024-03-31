def contar_frecuencia(lista):
    """
    Esta función cuenta la frecuencia de cada elemento en la lista.
    
    Parámetros:
    lista (list): Una lista de elementos.
    
    Retorna:
    dict: Un diccionario donde las claves son los elementos y los valores son las frecuencias.
    """
    frecuencia = {}  # Creamos un diccionario para almacenar las frecuencias de los elementos
    
    # Iteramos sobre cada elemento en la lista
    for elemento in lista:
        # Usamos el método get() para obtener el valor actual de la frecuencia del elemento.
        # Si el elemento no está en el diccionario, devuelve 0 y luego le sumamos 1.
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
    
    return frecuencia  # Devolvemos el diccionario de frecuencias

# Ejemplo de uso:
colores = ['rojo', 'verde', 'azul', 'rojo', 'verde', 'rojo']
print("Frecuencia de colores:", contar_frecuencia(colores))
