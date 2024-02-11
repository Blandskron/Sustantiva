equipaje = ("camisa", "zapatos", "pantalón", "zapatos", "vestido", "calcetines", "zapatos")

# Contamos cuántas veces aparece la palabra "zapatos" en la tupla "equipaje".
cantidad_zapatos = equipaje.count("zapatos")
print("Cantidad de zapatos en el equipaje:", cantidad_zapatos)

# Encontramos el índice de la primera aparición de "zapatos" en la tupla "equipaje".
primeros_zapatos = equipaje.index("zapatos")
print("Índice de los primeros zapatos en el equipaje:", primeros_zapatos)

# Iteramos sobre cada elemento en la tupla "equipaje" e imprimimos cada prenda.
for prenda in equipaje:
    print(prenda)
