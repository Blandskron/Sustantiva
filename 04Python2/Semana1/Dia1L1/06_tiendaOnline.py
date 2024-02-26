class TiendaOnline:
    def __init__(self, nombre, productos={}):
        """
        Constructor de la clase TiendaOnline.

        Args:
        - nombre (str): El nombre de la tienda en línea.
        - productos (dict): Un diccionario opcional de productos (por defecto, un diccionario vacío).
        """
        self.nombre = nombre    # Asigna el nombre de la tienda al atributo 'nombre'
        self.productos = productos  # Asigna el diccionario de productos proporcionado al atributo 'productos' (o crea un diccionario vacío si no se proporciona)

    def agregar_producto(self, nombre_producto, precio):
        """
        Método para agregar un producto a la tienda en línea.

        Args:
        - nombre_producto (str): El nombre del producto a agregar.
        - precio (float): El precio del producto.
        """
        self.productos[nombre_producto] = precio  # Agrega el producto al diccionario de productos de la tienda
        print(f"Se agregó {nombre_producto} a {self.nombre} por {precio}.")

    def mostrar_productos(self):
        """Método para mostrar los productos en la tienda en línea."""
        print(f"Productos en {self.nombre}:")
        for producto, precio in self.productos.items():
            print(f"- {producto}: ${precio}")  # Imprime cada producto y su precio

# Crear una instancia de TiendaOnline
amazon = TiendaOnline("Amazon")  # Crea una instancia de TiendaOnline con nombre "Amazon"

# Agregar productos a la tienda en línea
amazon.agregar_producto("Smartphone", 699)
amazon.agregar_producto("Tablet", 299)

# Mostrar los productos en la tienda en línea
amazon.mostrar_productos()
