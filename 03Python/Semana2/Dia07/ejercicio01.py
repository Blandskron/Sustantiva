# Definición de dos listas, una de números y otra de letras
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

# Itera sobre cada elemento de la lista 'numeros'
for n in numeros:
    print(n)  # Imprime el número actual
    # Itera sobre cada elemento de la lista 'letras' dentro del bucle de números
    for l in letras:
        print(l)  # Imprime la letra actual
