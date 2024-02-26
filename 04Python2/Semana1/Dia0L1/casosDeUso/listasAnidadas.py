def recorrer_lista_anidada(lista_anidada):
    # Itera sobre los elementos de la lista anidada
    for elemento in lista_anidada:
        # Verifica si el elemento es una lista
        if type(elemento) == list: 
            # Si el elemento es una lista, itera sobre sus elementos e imprímelos
            for item in elemento:
                print(item)
        else:
            # Si el elemento no es una lista, simplemente imprímelo
            print(elemento)

# Lista anidada para ser recorrida e impresa
lista_anidada = [
    [1, 2, 3],
    ["a", "b", "c"],
    ["q", "w", "e"]
]

# Llama a la función para recorrer e imprimir la lista anidada
recorrer_lista_anidada(lista_anidada)

# Otra lista anidada con elementos que no son listas
lista_anidada = [[1, 2, 3], 4, 5, 6]

# Llama a la función para recorrer e imprimir esta otra lista anidada
recorrer_lista_anidada(lista_anidada)
