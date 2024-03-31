class Libro:
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Cantidad: {self.cantidad}"


class Socio:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Socio: {self.nombre} - Dirección: {self.direccion} - Teléfono: {self.telefono}"


class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_al_catalogo(self, libro):
        self.libros.append(libro)

    def eliminar_del_catalogo(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro {libro.titulo} eliminado del catálogo")
        else:
            print(f"El libro {libro.titulo} no está en el catálogo")

    def buscar_libros(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None


class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.catalogo = Catalogo()
        self.socios = []

    def actualizacion_informacion(self, direccion, telefono):
        self.direccion = direccion
        self.telefono = telefono

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def ediciones_libro(self, libro, cantidad):
        libro.cantidad += cantidad

    def informacion_socios(self):
        print(f"Información de Socios de la Biblioteca {self.nombre}:")
        for socio in self.socios:
            print(socio)

    def buscar_libro(self, titulo):
        return self.catalogo.buscar_libros(titulo)

    def devolver_libro(self, socio, libro):
        libro.cantidad += 1
        print(f"El socio {socio.nombre} ha devuelto el libro {libro.titulo}")


# Creación de libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 5)
libro2 = Libro("1984", "George Orwell", 3)

# Creación de socios
socio1 = Socio("Juan", "Calle Principal 123", "123456789")
socio2 = Socio("María", "Avenida Central 456", "987654321")

# Creación de una biblioteca
biblioteca1 = Biblioteca("Biblioteca Central", "Calle Central 789", "555-1234")
biblioteca1.catalogo.agregar_al_catalogo(libro1)
biblioteca1.catalogo.agregar_al_catalogo(libro2)
biblioteca1.agregar_socio(socio1)
biblioteca1.agregar_socio(socio2)

# Buscar libro en el catálogo
print(biblioteca1.buscar_libro("Cien años de soledad"))

# Devolver libro por socio
libro_prestado = biblioteca1.buscar_libro("1984")
if libro_prestado:
    biblioteca1.devolver_libro(socio2, libro_prestado)

# Información de socios
biblioteca1.informacion_socios()
