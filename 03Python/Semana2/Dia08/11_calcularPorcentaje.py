def calcular_valor_bruto_descuento(valor_liquido):
    # Calcula el valor bruto (100%)
    valor_bruto = valor_liquido / 0.8625

    # Calcula el valor del descuento (13.75%)
    valor_descuento = valor_bruto - valor_liquido

    return valor_bruto, valor_descuento

if __name__ == "__main__":
    try:
        valor_liquido = float(input("Ingrese el valor líquido: "))
        valor_bruto, valor_descuento = calcular_valor_bruto_descuento(valor_liquido)
        print(f"El valor bruto es: {valor_bruto}")
        print(f"El valor del descuento es: {valor_descuento}")
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
