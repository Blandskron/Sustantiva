# Creamos un conjunto anidado utilizando frozenset (conjuntos inmutables).
# Cada elemento del conjunto principal es un frozenset que contiene un conjunto de frutas.
conjunto_anidado = {frozenset({'manzana', 'plátano', 'naranja'}), frozenset({'pera', 'uva', 'mango'})}

# Agregamos un nuevo conjunto al conjunto anidado.
# Creamos un nuevo frozenset con el conjunto {'piña', 'kiwi', 'papaya'} y lo agregamos al conjunto principal.
conjunto_anidado.add(frozenset({'piña', 'kiwi', 'papaya'}))
print("Después de agregar un nuevo conjunto:", conjunto_anidado)

# Eliminamos un conjunto del conjunto anidado.
# Eliminamos el frozenset que contiene el conjunto {'manzana', 'plátano', 'naranja'} del conjunto principal.
conjunto_anidado.remove(frozenset({'manzana', 'plátano', 'naranja'}))
print("Después de eliminar un conjunto:", conjunto_anidado)
