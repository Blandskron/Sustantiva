# Definición de la función mezclar_ingredientes() que acepta un número variable de argumentos
def mezclar_ingredientes(*ingrediente):
    # Imprime el primer ingrediente que se va a mezclar
    print(f"Mezclando el ingrediente: {ingrediente[0]}")
    # Imprime el segundo ingrediente que se va a mezclar
    print(f"Mezclando el ingrediente: {ingrediente[1]}")

# Llamada a la función mezclar_ingredientes() con varios ingredientes
mezclar_ingredientes("harina", "azúcar", "leche", "huevos")
