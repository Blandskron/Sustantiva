# Definir un diccionario para traducir palabras de inglés a español
traductor = {
    "hello": "hola",
    "apple": "manzana",
    "dog": "perro",
    "cat": "gato"
}

# Traducir una palabra de inglés a español
palabra = "dog"
traduccion = traductor.get(palabra, "La palabra no está en el diccionario")

# Imprimir la traducción de la palabra
print(f"La traducción de '{palabra}' es '{traduccion}'")
