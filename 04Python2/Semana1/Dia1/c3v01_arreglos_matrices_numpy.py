import numpy as np

lista = [1, 2, 3]
lista_anidada = [[1, 2, 3], [4, 5, 6]]

arreglo = np.array(lista)
print(arreglo)

matriz = np.array(lista_anidada)
print(matriz)

matriz = np.matrix(lista_anidada)
print(matriz)

matriz_ceros = np.zeros((2, 3))
print(matriz_ceros)
