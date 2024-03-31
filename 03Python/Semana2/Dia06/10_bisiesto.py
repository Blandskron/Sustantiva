# Pedir al usuario que ingrese un año y convertir la entrada a tipo entero
anio = int(input("Ingrese un año: "))

# Verificar si el año es divisible por 4 y no es divisible por 100,
# o si es divisible por 400, lo que indica que es un año bisiesto.
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    # Imprimir un mensaje indicando que el año ingresado es bisiesto
    print(anio, "es un año bisiesto.")
else:
    # Si el año no cumple con las condiciones anteriores, no es bisiesto
    # Imprimir un mensaje indicando que el año ingresado no es bisiesto
    print(anio, "no es un año bisiesto.")
