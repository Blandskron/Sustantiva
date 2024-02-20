class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"


# Crear instancias de la clase Libro
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 432)

# Obtener información sobre los libros
print(libro1.info())  # Imprime: Título: El principito, Autor: Antoine de Saint-Exupéry, Páginas: 96
print(libro2.info())  # Imprime: Título: Cien años de soledad, Autor: Gabriel García Márquez, Páginas: 432
