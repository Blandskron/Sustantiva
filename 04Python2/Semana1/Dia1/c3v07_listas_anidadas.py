def recorrer_lista_anidada(lista_anidada):

    for elemento in lista_anidada:
        if type(elemento) == list: 
            for item in elemento:
                print(item)
        else:
            print(elemento)


lista_anidada = [
    [1, 2, 3],
    ["a", "b", "c"],
    ["q", "w", "e"]
]
recorrer_lista_anidada(lista_anidada)

lista_anidada = [[1, 2, 3], 4, 5, 6]
recorrer_lista_anidada(lista_anidada)
