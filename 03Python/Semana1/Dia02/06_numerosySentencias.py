# Solicitar al usuario ingresar un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
