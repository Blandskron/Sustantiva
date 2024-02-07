# Programa para calcular el precio total de una compra en una tienda de comestibles

# Inicializamos una variable para almacenar el precio total
total = 0

# Solicitamos al usuario que ingrese la cantidad de artículos que desea comprar
num_articulos = int(input("Ingrese el número de artículos que desea comprar: "))

# Iteramos a través de cada artículo para solicitar su nombre y precio
for i in range(num_articulos):
    nombre_articulo = input(f"Ingrese el nombre del artículo {i+1}: ")
    precio_articulo = float(input(f"Ingrese el precio del artículo {i+1}: $"))
    
    # Agregamos el precio del artículo al total
    total += precio_articulo

# Mostramos el precio total de la compra
print(f"El precio total de su compra es: ${total:.2f}")
