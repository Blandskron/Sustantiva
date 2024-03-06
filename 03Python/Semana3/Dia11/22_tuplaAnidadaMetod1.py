# Creamos una tupla anidada llamada 'tupla_anidada'
# donde cada elemento de la tupla principal es una tupla interna.
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Acceder a un elemento específico de la tupla anidada.
# En este caso, accedemos al segundo elemento (índice 1) de la primera tupla (índice 0).
print("El segundo elemento de la primera tupla es:", tupla_anidada[0][1])

# Encontrar la longitud de la tupla anidada.
print("La longitud de la tupla anidada es:", len(tupla_anidada))

# Encontrar el índice de un elemento en una tupla anidada.
# Buscamos el índice del número 5 en la segunda tupla (índice 1).
indice = tupla_anidada[1].index(5)
print("El índice de 5 en la segunda tupla es:", indice)

# Concatenar tuplas.
# Creamos una nueva tupla concatenando 'tupla_anidada' con una nueva tupla ((10, 11, 12)).
tupla_concatenada = tupla_anidada + ((10, 11, 12),)
print("Tupla concatenada:", tupla_concatenada)

# Encontrar el máximo de una tupla anidada.
# Usamos la función max() dos veces para encontrar el máximo valor en 'tupla_anidada'.
maximo = max(max(tupla_anidada))
print("El máximo de la tupla anidada es:", maximo)
