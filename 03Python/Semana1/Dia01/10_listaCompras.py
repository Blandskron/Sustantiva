# Crear una lista vacía para almacenar elementos de la lista de compras
lista_compras = []

# Ciclo interactivo para agregar elementos a la lista de compras
while True:
    # Solicitar al usuario ingresar un artículo de la lista de compras
    articulo = input("Ingrese un artículo (o escriba 'fin' para terminar): ")
    
    # Verificar si el usuario quiere terminar de agregar artículos
    if articulo.lower() == 'fin':
        break  # Salir del bucle si el usuario escribe 'fin'
    
    # Agregar el artículo a la lista de compras
    lista_compras.append(articulo)

# Imprimir la lista de compras
print("Lista de compras:")
for item in lista_compras:
    print("-", item)
