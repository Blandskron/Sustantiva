class Product:
    def __init__(self, name, price, quantity):
        """
        Constructor de la clase Product.
        
        Args:
        - name (str): Nombre del producto.
        - price (float): Precio del producto.
        - quantity (int): Cantidad disponible del producto.
        """
        self.name = name  # Establece el nombre del producto
        self.price = price  # Establece el precio del producto
        self.quantity = quantity  # Establece la cantidad disponible del producto
