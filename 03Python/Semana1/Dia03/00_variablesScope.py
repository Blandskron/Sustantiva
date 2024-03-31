# Variables
x = 10
y = "Hola, mundo!"
z = 3.14
is_true = True

# Imprimir variables
print(x)
print(y)
print(z)
print(is_true)

# Ámbito global
global_var = 20

def my_function():
    # Ámbito local
    local_var = 30
    print("Variable global dentro de la función:", global_var)
    print("Variable local dentro de la función:", local_var)

my_function()

# Esto dará un error porque local_var está definida solo dentro de la función.
# print("Intentando acceder a variable local fuera de la función:", local_var)

# El "built-in scope" se refiere al ámbito de las variables y funciones integradas directamente en el intérprete de Python. Estas son funciones y objetos que están disponibles globalmente en cualquier parte del código sin necesidad de importar módulos adicionales. Son parte del conjunto básico de funcionalidades proporcionadas por Python.

# Algunos ejemplos de elementos en el "built-in scope" incluyen:

# Funciones incorporadas como print(), len(), range(), etc.
# Tipos de datos incorporados como int, str, list, tuple, set, dict, etc.
# Excepciones incorporadas como TypeError, ValueError, etc.
# Estas funciones y tipos de datos están disponibles sin necesidad de importar ningún módulo específico. Puedes utilizarlos directamente en cualquier parte de tu código Python. La presencia de este "built-in scope" facilita la escritura de código, ya que proporciona un conjunto básico de herramientas y funcionalidades que se pueden utilizar sin configuraciones adicionales.