# Importar la biblioteca NumPy con el alias np
import numpy as np

# Crear una lista simple
lista = [1, 2, 3]

# Crear una lista anidada
lista_anidada = [[1, 2, 3], [4, 5, 6]]

# Crear un arreglo unidimensional a partir de la lista simple
arreglo = np.array(lista)
print(arreglo)  # Imprimir el arreglo unidimensional

# Crear una matriz bidimensional a partir de la lista anidada usando np.array
matriz = np.array(lista_anidada)
print(matriz)  # Imprimir la matriz bidimensional

# Crear una matriz bidimensional a partir de la lista anidada usando np.matrix
matriz = np.matrix(lista_anidada)
print(matriz)  # Imprimir la matriz bidimensional

# Crear una matriz de ceros con 2 filas y 3 columnas
matriz_ceros = np.zeros((2, 3))
print(matriz_ceros)  # Imprimir la matriz de ceros
