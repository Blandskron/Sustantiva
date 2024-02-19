"""
matriz = [[1, 2],
          [3, 4],
          [5, 6]]

La diagonal se compone por los números 1 y 4

transpuesta = [[1, 3, 5],
               [2, 4, 6],

"""

import numpy as np


matriz = np.array([[1, 2], [3, 4], [5, 6]])

transpuesta = matriz.transpose()
print(transpuesta)
