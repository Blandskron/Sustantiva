# Definición de la variable global 'contador'
contador = 0  # Variable global

# Definición de la función incrementar_contador()
def incrementar_contador():
    global contador  # Utiliza la variable global dentro de la función
    contador += 1

# Incrementa el contador global llamando a la función incrementar_contador()
incrementar_contador()

# Imprime el valor del contador global después de ser incrementado
print(contador)
