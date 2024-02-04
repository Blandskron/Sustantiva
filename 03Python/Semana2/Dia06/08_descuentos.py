# Calcular el descuento en una tienda
monto_compra = float(input("Ingrese el monto total de la compra: "))

if monto_compra > 100:
    descuento = 0.1 * monto_compra  # 10% de descuento si la compra es mayor a $100
else:
    descuento = 0

total_a_pagar = monto_compra - descuento
print("Total a pagar después del descuento:", total_a_pagar)
