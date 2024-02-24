class TiendaOnline:
    def __init__(self, nombre, productos={}):
        self.nombre = nombre
        self.productos = productos

    def agregar_producto(self, nombre_producto, precio):
        self.productos[nombre_producto] = precio
        print(f"Se agregó {nombre_producto} a {self.nombre} por {precio}.")

    def mostrar_productos(self):
        print(f"Productos en {self.nombre}:")
        for producto, precio in self.productos.items():
            print(f"- {producto}: ${precio}")

# Crear una instancia de TiendaOnline
amazon = TiendaOnline("Amazon")
amazon.agregar_producto("Smartphone", 699)
amazon.agregar_producto("Tablet", 299)
amazon.mostrar_productos()
