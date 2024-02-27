# Definición de la función mezclar_ingredientes()
def mezclar_ingredientes(ingredientes):
    # Itera sobre cada ingrediente en la lista de ingredientes
    for ingrediente in ingredientes:
        # Imprime el mensaje indicando que se está mezclando el ingrediente actual
        print(f"Mezclando el ingrediente: {ingrediente}")

# Lista de ingredientes que se van a mezclar
ingredientes = ["harina", "azúcar", "huevos", "leche", "polvo para hornear", "mantequilla", "mantequilla"]

# Llama a la función mezclar_ingredientes() con la lista de ingredientes como argumento
mezclar_ingredientes(ingredientes)
