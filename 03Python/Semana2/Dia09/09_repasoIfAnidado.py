# Solicitar al usuario que ingrese un número y convertirlo a entero
numero = int(input("Ingresar un número: "))

# Usando múltiples declaraciones if-else
if numero > 0:
    # Verificar si el número es mayor que 0 e imprimir un mensaje si es positivo
    print("El número es positivo")
else:
    # Si el número no es positivo, anidamos otra declaración if para verificar si es igual a 0
    if numero == 0:
        # Imprimir un mensaje si el número es igual a 0
        print("El número es igual a 0")
    else:
        # Si el número no es igual a 0, se considera negativo y se imprime un mensaje
        print("El número es negativo")

# Usando elif para condiciones múltiples
if numero > 0:
    # Verificar si el número es positivo e imprimir un mensaje si es positivo
    print("El número es positivo")
elif numero == 0:
    # Verificar si el número es igual a 0 e imprimir un mensaje si es igual a 0
    print("El número es igual a 0")
else:
    # Si el número no es ni positivo ni igual a 0, se considera negativo y se imprime un mensaje
    print("El número es negativo")
