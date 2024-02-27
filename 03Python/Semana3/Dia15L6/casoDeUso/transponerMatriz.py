"""
matriz = [[1, 2],
          [3, 4],
          [5, 6]]

La diagonal se compone por los números 1 y 4

transpuesta = [[1, 3, 5],
               [2, 4, 6],

"""

import numpy as np

# Definir la matriz como un arreglo de NumPy
matriz = np.array([[1, 2], [3, 4], [5, 6]])

# Calcular la transpuesta de la matriz
transpuesta = matriz.transpose()

# Imprimir la matriz transpuesta
print(transpuesta)
