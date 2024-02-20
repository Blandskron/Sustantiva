# Definición de la función hacer_pedido() con parámetros con valores predeterminados
def hacer_pedido(tipo_de_pastel="Chocolate", cantidad_porciones=10):
    # Imprime el tipo de pastel y la cantidad de porciones
    print(f"Tipo de pastel: {tipo_de_pastel}. Cantidad de porciones: {cantidad_porciones}.")

# Llamadas a la función hacer_pedido() con diferentes argumentos
hacer_pedido("Vainilla", 5)  # Especifica un tipo de pastel y una cantidad de porciones
hacer_pedido()  # No especifica argumentos, por lo que se utilizan los valores predeterminados
hacer_pedido(tipo_de_pastel="Fresa")  # Especifica solo el tipo de pastel, utiliza la cantidad de porciones predeterminada
hacer_pedido(cantidad_porciones=15)  # Especifica solo la cantidad de porciones, utiliza el tipo de pastel predeterminado
