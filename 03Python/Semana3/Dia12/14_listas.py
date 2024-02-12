# Definición de una lista de números
numeros = [1, 2, 3, 4, 5]

# Recorrido e impresión de los elementos de la lista
print("Elementos de la lista:")
for numero in numeros:
    print(numero)

# Agregar un elemento a la lista
numeros.append(6)
print("Lista después de agregar un elemento:", numeros)

# Eliminar un elemento de la lista
numeros.remove(3)
print("Lista después de eliminar el elemento 3:", numeros)
