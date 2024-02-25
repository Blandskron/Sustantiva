class Libro:
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro.

        Args:
        - titulo (str): El título del libro.
        - autor (str): El autor del libro.
        - paginas (int): El número de páginas del libro.
        """
        self.titulo = titulo    # Asigna el título del libro al atributo 'titulo'
        self.autor = autor      # Asigna el autor del libro al atributo 'autor'
        self.paginas = paginas  # Asigna el número de páginas del libro al atributo 'paginas'

    def info(self):
        """
        Método para obtener información sobre el libro.

        Returns:
        - str: Una cadena que contiene el título, el autor y el número de páginas del libro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"


# Crear instancias de la clase Libro
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)  # Crea una instancia de Libro con los datos del libro "El principito"
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 432)  # Crea una instancia de Libro con los datos del libro "Cien años de soledad"

# Obtener información sobre los libros
print(libro1.info())  # Imprime: Título: El principito, Autor: Antoine de Saint-Exupéry, Páginas: 96
print(libro2.info())  # Imprime: Título: Cien años de soledad, Autor: Gabriel García Márquez, Páginas: 432
