# Solicita al usuario que ingrese el monto total de la compra
monto_compra = float(input("Ingrese el monto total de la compra: "))

# Comprueba si el monto de la compra es mayor que $100
if monto_compra > 100:
    descuento = 0.1 * monto_compra  # Calcula el 10% de descuento si la compra es mayor a $100
else:
    descuento = 0  # Si la compra es igual o menor a $100, no hay descuento

# Calcula el total a pagar restando el descuento del monto total de la compra
total_a_pagar = monto_compra - descuento

# Imprime el total a pagar después de aplicar el descuento
print("Total a pagar después del descuento:", total_a_pagar)
