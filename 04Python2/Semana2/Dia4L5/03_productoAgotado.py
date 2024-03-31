class ProductoAgotadoError(Exception):
    def __init__(self, producto):
        super().__init__(f"El producto {producto} está agotado.")

def verificar_stock(producto, stock):
    if stock == 0:
        raise ProductoAgotadoError(producto)

# Ejemplo de uso
try:
    producto = "Camiseta"
    stock = 0
    verificar_stock(producto, stock)
except ProductoAgotadoError as e:
    print("Error de stock:", e)
