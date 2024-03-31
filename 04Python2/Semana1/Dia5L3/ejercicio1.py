class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor}"


class Socio:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Socio: {self.nombre}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.socios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_catalogo(self):
        print(f"Catálogo de la Biblioteca {self.nombre}:")
        for libro in self.catalogo:
            print(libro)

    def mostrar_socios(self):
        print(f"Socios de la Biblioteca {self.nombre}:")
        for socio in self.socios:
            print(socio)


# Creación de libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")

# Creación de socios
socio1 = Socio("Juan")
socio2 = Socio("María")

# Creación de una biblioteca
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_socio(socio1)
biblioteca1.agregar_socio(socio2)

# Mostrar el catálogo de la biblioteca
biblioteca1.mostrar_catalogo()

# Mostrar los socios de la biblioteca
biblioteca1.mostrar_socios()
