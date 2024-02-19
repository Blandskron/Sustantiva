# Creamos una lista de listas llamada 'lista_palabras'
# donde cada lista interna contiene palabras.
lista_palabras = [['gato', 'perro', 'pájaro'], ['sol', 'luna', 'estrella'], ['rojo', 'verde', 'azul']]

# Acceder a un elemento específico de la lista de listas.
# En este caso, accedemos a la tercera palabra (índice 2) de la segunda lista (índice 1).
print("La tercera palabra de la segunda lista es:", lista_palabras[1][2])

# Agregar una nueva palabra ('pez') a la primera lista.
lista_palabras[0].append('pez')
print("Después de agregar 'pez' a la primera lista:", lista_palabras[0])

# Insertar una palabra ('amarillo') en una posición específica (índice 1) de la tercera lista.
lista_palabras[2].insert(1, 'amarillo')
print("Después de insertar 'amarillo' en la segunda posición de la tercera lista:", lista_palabras[2])

# Eliminar un elemento específico ('luna') de la segunda lista.
lista_palabras[1].remove('luna')
print("Después de eliminar 'luna' de la segunda lista:", lista_palabras[1])
