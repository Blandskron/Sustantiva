def calcular_iva():
    try:
        # El usuario ingresa el precio sin IVA y la tasa de IVA
        precio_sin_iva = float(input("Ingrese el precio del producto sin IVA: "))
        tasa_iva = float(input("Ingrese la tasa de IVA de su país (en porcentaje, ej. 16 para 16%): "))

        # Calculando el IVA y el precio total
        iva = precio_sin_iva * (tasa_iva / 100)
        precio_total_con_iva = precio_sin_iva + iva

        # Imprimiendo los resultados
        print(f"Precio sin IVA: {precio_sin_iva}")
        print(f"Valor del IVA: {iva}")
        print(f"Precio con IVA: {precio_total_con_iva}")

    except ValueError:
        print("Error: Por favor, ingrese valores numéricos.")

calcular_iva()
