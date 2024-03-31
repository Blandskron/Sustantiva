# Definición de una lista de números
numeros = [5, 13, 16, 7]

# Iteración sobre cada número en la lista 'numeros'
for numero in numeros:
    # Comprueba si el número es menor que 10
    if numero < 10:
        print("El numero", numero, "es menor que 10.")
    # Si no es menor que 10, comprueba si es menor que 15
    elif numero < 15:
        print("El numero", numero, "es menor que 15.")
    # Si no es menor que 15, entonces es mayor o igual a 15
    else:
        print("El numero", numero, "es mayor o igual a 15.")
