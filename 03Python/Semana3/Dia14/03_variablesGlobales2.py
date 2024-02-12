contador = 0  # Variable global

def incrementar_contador():
    global contador  # Utiliza la variable global dentro de la función
    contador += 1

incrementar_contador()  # Incrementa el contador global
print(contador)  # Imprime el valor del contador global
