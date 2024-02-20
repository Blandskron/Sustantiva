import numpy as np

# Definir las matrices a sumar y restar
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[1, 2], [3, 4]])

# Realizar la suma de las matrices
suma = np.add(matriz_a, matriz_b)
print(suma)  # Imprimir la suma de las matrices

# Realizar la resta de las matrices
resta = np.subtract(matriz_a, matriz_b)
print(resta)  # Imprimir la resta de las matrices

# Realizar el producto punto (producto de matrices) entre las matrices
punto = matriz_a.dot(matriz_b)
print(punto)  # Imprimir el producto punto de las matrices
