# Definición de dos listas de números
grupo1 = [5, 13, 16, 7]
grupo2 = [5, 14, 15, 20]

# Bucle anidado que itera sobre cada número en grupo1 y luego sobre cada número en grupo2
for numero1 in grupo1:
    for numero2 in grupo2:
        # Si los números son iguales, pasa a la siguiente iteración del bucle
        if numero1 == numero2:
            continue
        # Si el número en grupo1 es mayor que el número en grupo2, termina la iteración del bucle
        elif numero1 > numero2:
            break
        # Si el número en grupo1 es menor que el número en grupo2, imprime una conclusión
        else:
            print("Conclusion:", numero1, "es menor que", numero2)
