# Creamos una lista de listas llamada 'lista_numeros'
# donde cada lista interna contiene números enteros.
lista_numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acceder a un elemento específico de la lista de listas.
# En este caso, accedemos al segundo elemento (índice 1) de la primera lista (índice 0).
print("El segundo elemento de la primera lista es:", lista_numeros[0][1])

# Agregar un nuevo elemento (10) a la segunda lista.
lista_numeros[1].append(10)
print("Después de agregar 10 a la segunda lista:", lista_numeros[1])

# Extender la tercera lista con otra lista de números (11, 12, 13).
lista_numeros[2].extend([11, 12, 13])
print("Después de extender la tercera lista:", lista_numeros[2])

# Eliminar un elemento específico (2) de la primera lista.
lista_numeros[0].remove(2)
print("Después de eliminar 2 de la primera lista:", lista_numeros[0])
