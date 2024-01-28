# Imprimir todos los atributos del módulo dir
for attribute in dir():
    print(attribute)

import math

# Obtener la lista de nombres definidos en el módulo math
names = dir(math)

# Imprimir los nombres uno por uno
for name in names:
    print(name)
