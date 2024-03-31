def buscar_elemento(lista, elemento):
    if elemento not in lista:
        raise ValueError(f"El elemento {elemento} no está en la lista.")

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
def buscar_elemento(lista, elemento):
    if elemento not in lista:
        raise ValueError(f"El elemento {elemento} no está en la lista.")

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
try:
    buscar_elemento(mi_lista, 6)
except ValueError as e:
    print("Error:", e)
