# Ejemplo con if, elif y else

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")

# Verificar la longitud del nombre
if len(nombre) > 10:
    print("Tu nombre es largo.")
elif len(nombre) < 5:
    print("Tu nombre es corto.")
else:
    print("Tu nombre tiene una longitud moderada.")