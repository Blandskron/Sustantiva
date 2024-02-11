# Creamos un conjunto inicial de números
numeros = {1, 2, 3, 4, 5}

# Mostramos el conjunto de números antes de usar discard()
print("Conjunto de números:", numeros)

# Eliminamos el número 3 del conjunto usando discard()
numeros.discard(3)

# Mostramos el conjunto de números después de usar discard()
print("Conjunto de números después de descartar 3:", numeros)

# Intentamos eliminar un número que no está en el conjunto
numeros.discard(6)

# Mostramos el conjunto de números después de intentar descartar 6 (no debería haber cambios)
print("Conjunto de números después de intentar descartar 6:", numeros)
