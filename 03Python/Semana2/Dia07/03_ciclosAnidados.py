# Definición de dos listas de números
grupo1 = [5, 13, 16]
grupo2 = [5, 14]

# Bucle anidado que itera sobre cada número en el grupo1 y luego sobre cada número en el grupo2
for numero1 in grupo1:
    for numero2 in grupo2:
        # Imprime cada combinación de números obtenida de los dos grupos
        print(numero1, numero2)
