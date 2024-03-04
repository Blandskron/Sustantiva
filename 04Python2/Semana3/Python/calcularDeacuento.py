def calcular_descuento_interactivo():
    """
    Función para calcular el descuento de forma interactiva, permitiendo al usuario ingresar el precio original
    y el porcentaje de descuento.
    """
    try:
        precio_original = float(input("Ingrese el precio original: "))
        porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

        valor_descuento = precio_original * (porcentaje_descuento / 100)
        precio_final = precio_original - valor_descuento

        print(f"\nValor Real: {precio_original}")
        print(f"Valor del Descuento: {valor_descuento}")
        print(f"Precio con Descuento: {precio_final}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

# Llamando a la función para realizar el cálculo de forma interactiva
calcular_descuento_interactivo()
