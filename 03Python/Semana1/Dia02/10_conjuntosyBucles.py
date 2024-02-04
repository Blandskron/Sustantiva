# Definir dos conjuntos de números
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Mostrar los números comunes en ambos conjuntos
print("Números comunes en ambos conjuntos:")
for numero in conjunto1 & conjunto2:
    print(numero)
