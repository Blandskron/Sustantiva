# Creamos un diccionario llamado 'tienda' que contiene diferentes secciones de productos (frutas, verduras, bebidas),
# donde cada sección es un diccionario que mapea productos a su cantidad disponible.
tienda = {
    'frutas': {'manzanas': 10, 'bananas': 20, 'uvas': 15},
    'verduras': {'zanahorias': 25, 'espinacas': 30, 'cebollas': 20},
    'bebidas': {'agua': 50, 'refrescos': 40, 'jugo': 35}
}

# Mostrar todas las frutas disponibles en la tienda
print("Las frutas disponibles son:", tienda['frutas'])

# Obtener la cantidad de zanahorias en la tienda
print("La cantidad de zanahorias en la tienda es:", tienda['verduras']['zanahorias'])

# Agregar un nuevo producto a la sección de bebidas
tienda['bebidas']['café'] = 25
print("Después de agregar café, las bebidas disponibles son:", tienda['bebidas'])

# Eliminar una bebida de la tienda (refrescos)
del tienda['bebidas']['refrescos']
print("Después de eliminar refrescos, las bebidas restantes son:", tienda['bebidas'])
