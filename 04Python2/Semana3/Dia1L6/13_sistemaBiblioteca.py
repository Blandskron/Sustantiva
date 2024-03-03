class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}"


class Libro:
    def __init__(self, titulo, isbn, autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor

    def __str__(self):
        return f"Libro: {self.titulo}, ISBN: {self.isbn}, Autor: {self.autor}"


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f"Prestamo - Libro: {self.libro.titulo}, Usuario: {self.usuario}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"
