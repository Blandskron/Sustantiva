# Lista de productos en un supermercado
productos = ["Frutas y Verduras", "Carnes y Aves", "Pescados y Mariscos", "Lácteos", "Panadería"]

# Imprime un mensaje inicial para indicar que se mostrará la ruta ideal de compras
print("Tu ruta ideal de compras:")

# Itera sobre la lista de productos utilizando la función enumerate()
# La función enumerate() devuelve tanto el índice como el elemento de la lista en cada iteración
# El parámetro start=1 indica que los índices comienzan desde 1 en lugar de 0
for i, producto in enumerate(productos, start=1):
    # Imprime el índice y el nombre del producto, utilizando una f-string para formatear el mensaje
    print(f"{i}. {producto}")
