# Definición de la función calculate_discounted_price() que calcula el precio descontado
def calculate_discounted_price(price, discount):
    # Verifica si el precio y el descuento son números
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("El precio y el descuento deben ser números")

    # Verifica si el precio y el descuento son valores positivos
    if price < 0 or discount < 0:
        raise ValueError("El precio y el descuento deben ser valores positivos")

    try:
        # Calcula el precio descontado
        discounted_price = price - (price * discount)
        return discounted_price

    except Exception as e:
        # Captura cualquier error inesperado y lo lanza como una excepción
        raise Exception("Ha ocurrido un error inesperado: " + str(e))

# Llamada a la función calculate_discounted_price() con un precio y un descuento
response = calculate_discounted_price(100, 0.2)

# Imprime el precio descontado
print(response)
