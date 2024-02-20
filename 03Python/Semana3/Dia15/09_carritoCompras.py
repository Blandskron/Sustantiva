from productos import Product  # Importa la clase Product desde el archivo product.py

# Clase Article que hereda de Product
class Article(Product):
    def addToCart(self):
        return f"Agregando {self.quantity} unidades del artículo {self.name}"

# Clase Service que hereda de Product
class Service(Product):
    def addToCart(self):
        return f"Agregando el servicio {self.name} al carrito"

# Clase Cart que gestiona los productos agregados al carrito
class Cart:
    def __init__(self):
        self.products = []  # Inicializa una lista vacía para almacenar los productos en el carrito

    # Método para agregar un producto al carrito
    def addProduct(self, product):
        product.addToCart()  # Llama al método addToCart del producto
        self.products.append(product)  # Agrega el producto a la lista de productos en el carrito

    # Método para eliminar un producto del carrito
    def deleteProduct(self, product):
        self.products = [item for item in self.products if item.name != product.name]  # Filtra los productos

    # Método para calcular el total de la compra
    def calculateTotal(self):
        total = sum(item.price * item.quantity for item in self.products)  # Calcula el total
        return total

    # Método para obtener los productos en el carrito
    def getProducts(self):
        return self.products  # Devuelve la lista de productos en el carrito

# Creación de instancias de productos
book = Article("Libro", 100, 2)
course = Service("Curso", 120, 1)

# Creación de una instancia de carrito
cart = Cart()

# Agrega productos al carrito
cart.addProduct(book)
cart.addProduct(course)

# Calcula el total de la compra
total = cart.calculateTotal()
print(total)
