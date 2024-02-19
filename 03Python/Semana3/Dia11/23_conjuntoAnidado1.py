# Creamos un conjunto anidado utilizando frozenset (conjuntos inmutables).
# Cada elemento del conjunto principal es un frozenset que contiene un conjunto de números.
conjunto_anidado = {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9})}

# Iteramos sobre los conjuntos anidados e imprimimos cada conjunto.
for conjunto in conjunto_anidado:
    print(conjunto)

# Agregamos un nuevo conjunto al conjunto anidado.
# Creamos un nuevo frozenset con el conjunto {10, 11, 12} y lo agregamos al conjunto principal.
conjunto_anidado.add(frozenset({10, 11, 12}))
print("Después de agregar un nuevo conjunto:", conjunto_anidado)

# Eliminamos un conjunto del conjunto anidado.
# Eliminamos el frozenset que contiene el conjunto {7, 8, 9} del conjunto principal.
conjunto_anidado.remove(frozenset({7, 8, 9}))
print("Después de eliminar un conjunto:", conjunto_anidado)
