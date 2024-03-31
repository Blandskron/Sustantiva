# Solicitar al usuario que ingrese un número y convertirlo a entero
numero = int(input("Ingresar un número: "))

# Verificar si el número es positivo
if numero > 0:
    # Si el número es mayor que 0, imprimir un mensaje indicando que es positivo
    print("El número es positivo")
else:
    # Si el número no es mayor que 0 (es igual a 0 o negativo), imprimir un mensaje indicando que no es positivo
    print("El número no es positivo")
