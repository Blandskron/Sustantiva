def contar_frecuencia(lista):
    """Esta función cuenta la frecuencia de cada elemento en la lista."""
    frecuencia = {}
    for elemento in lista:
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
    return frecuencia

# Ejemplo de uso:
colores = ['rojo', 'verde', 'azul', 'rojo', 'verde', 'rojo']
print("Frecuencia de colores:", contar_frecuencia(colores))
