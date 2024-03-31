# Definir un diccionario de edades
edades = {"Juan": 25, "María": 30, "Carlos": 22, "Ana": 27}

# Solicitar al usuario ingresar un nombre
nombre = input("Ingrese un nombre: ")

# Verificar si el nombre está en el diccionario y mostrar su edad
if nombre in edades:
    print(f"{nombre} tiene {edades[nombre]} años.")
else:
    print(f"No se encontró la edad de {nombre}.")
