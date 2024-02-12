# Definición de un conjunto de colores
colores = {"rojo", "azul", "verde", "amarillo"}

# Recorrido e impresión de los elementos del conjunto
print("Elementos del conjunto:")
for color in colores:
    print(color)

# Agregar un nuevo color al conjunto
colores.add("blanco")
print("Conjunto después de agregar blanco:", colores)

# Eliminar un color del conjunto
colores.remove("verde")
print("Conjunto después de eliminar verde:", colores)
