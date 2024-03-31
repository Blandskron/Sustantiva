# Definición de una función llamada calculate_tip que toma dos argumentos:
# - bill_amount: la cantidad total de la factura
# - tipPercentage: el porcentaje de propina que se desea dejar
def calculate_tip(bill_amount, tipPercentage):
    # Calcula la propina multiplicando el monto de la factura por el porcentaje de propina.
    # Primero, se divide el porcentaje entre 100 para convertirlo en un valor decimal.
    # Luego, se multiplica por el monto de la factura para obtener la cantidad de propina.
    tip = bill_amount * (tipPercentage / 100)
    # Redondea el valor de la propina a dos decimales.
    # Esto es útil para tener un valor de propina con dos dígitos después del punto decimal.
    return round(tip, 2)

# Llama a la función calculate_tip con un monto de factura de $100 y un porcentaje de propina del 10%.
# La función devuelve el valor calculado de la propina.
response = calculate_tip(100, 10)

# Imprime el valor de respuesta, que es la propina calculada.
print(response)
