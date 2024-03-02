try:
    # División por cero
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

try:
    # Índice fuera de rango
    lista = [1, 2, 3]
    elemento = lista[5]
except IndexError:
    print("Error: Índice fuera de rango")

try:
    # Tipos de datos no compatibles
    x = "Hola"
    y = int(x)
except ValueError:
    print("Error: No se puede convertir a entero")

try:
    # Acceso a un archivo que no existe
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError:
    print("Error: Archivo no encontrado")

try:
    # Llave no encontrada en un diccionario
    diccionario = {"clave": "valor"}
    valor = diccionario["otra_clave"]
except KeyError:
    print("Error: Clave no encontrada en el diccionario")

try:
    # Error de sintaxis
    eval("print('Hola mundo'")
except SyntaxError:
    print("Error: Error de sintaxis")

try:
    # Intento de acceder a un atributo o método inexistente
    class MiClase:
        pass

    objeto = MiClase()
    objeto.metodo_inexistente()
except AttributeError:
    print("Error: Atributo o método inexistente")
