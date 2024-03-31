# Solicita al usuario que ingrese el primer número
num1 = int(input("Ingrese el primer numero (1 de 3):\n"))

# Solicita al usuario que ingrese el segundo número
num2 = int(input("Ingrese el segundo numero (2 de 3):\n"))

# Solicita al usuario que ingrese el tercer número
num3 = int(input("Ingrese el tercer numero (3 de 3):\n"))

# Comprueba si el primer número es el mayor de los tres
if num1 > num2 and num1 > num3:
    print("\nEl numero mayor de los tres es:", num1)
# Comprueba si el segundo número es el mayor de los tres
elif num2 > num1 and num2 > num3:
    print("\nEl numero mayor de los tres es:", num2)
# Si ninguno de los dos casos anteriores se cumple, el tercer número es el mayor
else:
    print("\nEl numero mayor de los tres es:", num3)
