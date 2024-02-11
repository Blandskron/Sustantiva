# Definición de una función llamada print_triangle que imprime un triángulo de cierto tamaño y con un carácter dado.
# Toma dos argumentos:
# - size: el tamaño del triángulo (número de filas).
# - character: el carácter con el que se construye el triángulo.
def print_triangle(size, character):
    # Inicialización de una cadena vacía para almacenar el triángulo.
    triangle = ""
    
    # Bucle para iterar sobre cada fila del triángulo.
    for i in range(1, size + 1):
        # Cálculo del número de espacios en blanco antes de los caracteres del triángulo.
        spaces = " " * (size - i)
        # Construcción de una fila del triángulo con el carácter dado.
        line = character * (2 * i - 1)
        
        # Si es la última fila del triángulo, no se agrega un salto de línea al final.
        if i == size:
            triangle += spaces + line
        else:
            # Si no es la última fila, se agrega un salto de línea al final de la fila.
            triangle += spaces + line + "\n"
    
    # Devuelve el triángulo construido como una cadena.
    return triangle

# Llama a la función print_triangle con un tamaño de 3 y utilizando el carácter '*'.
# La función devuelve el triángulo construido como una cadena.
triangle = print_triangle(3, "*")

# Imprime el triángulo construido.
print(triangle)
