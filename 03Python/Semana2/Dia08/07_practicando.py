'''
    En este código, vamos a sumar el valor de las variables
    numero_1
    numero_2
    Sin embargo, el valor de estas variables es ingresado por el usuario.
'''
# La suma de dos números
print("Suma de dos números")

# Se solicita al usuario que ingrese el valor del primer número y se guarda en la variable numero_1
numero_1 = input("Intro número uno: ") # El input nos ayuda a ingresar valores desde el teclado

# Se solicita al usuario que ingrese el valor del segundo número y se guarda en la variable numero_2
numero_2 = input("Intro número dos: ")

# Se convierten los valores ingresados por el usuario a enteros (int) y se suman
resultado_suma = int(numero_1) + int(numero_2)

# Se imprime el resultado de la suma utilizando una f-string para formatear el mensaje
print(f"El resultado de la suma es: {resultado_suma}")
