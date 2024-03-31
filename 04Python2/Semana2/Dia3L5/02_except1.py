def obtener_elemento(lista, indice):
    try:
        elemento = lista[indice]
        print("El elemento en el índice", indice, "es:", elemento)
    except IndexError:
        print("Error: Índice fuera de rango.")

# Ejemplo de uso
mi_lista = [1, 2, 3]
obtener_elemento(mi_lista, 5)
