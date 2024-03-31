# Creamos un diccionario con algunas parejas clave-valor
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Obtenemos el valor asociado con la clave "nombre"
nombre = mi_diccionario.get("nombre")
print("Nombre:", nombre)

# Intentamos obtener el valor asociado con la clave "profesion"
# Como "profesion" no existe en el diccionario, get() devuelve None
profesion = mi_diccionario.get("profesion")
print("Profesión:", profesion)

# También podemos especificar un valor predeterminado si la clave no existe
# En este caso, si "profesion" no existe, se devolverá "Desconocido"
profesion = mi_diccionario.get("profesion", "Desconocido")
print("Profesión (con valor predeterminado):", profesion)
