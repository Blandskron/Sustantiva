# Creamos un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Obtenemos los pares clave-valor del diccionario utilizando el método items()
items = mi_diccionario.items()

# Iteramos sobre los pares clave-valor y los imprimimos
print("Pares clave-valor del diccionario:")
for clave, valor in items:
    print(f"Clave: {clave}, Valor: {valor}")
