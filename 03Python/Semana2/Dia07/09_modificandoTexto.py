# Definición de una cadena de texto
frase = "La programación es el arte de crear soluciones con código"

# Obtención del largo de la cadena (número de caracteres)
largo = len(frase)
print(largo)

# Convertir la cadena a mayúsculas
frase_mayuscula = frase.upper()
print(frase_mayuscula)

# Convertir la cadena a minúsculas
frase_minuscula = frase.lower()
print(frase_minuscula)

# Reemplazar una parte de la cadena con otra
nueva_frase = frase.replace("crear soluciones", "resolver problemas")
print(nueva_frase)

# Dividir la cadena en una lista de palabras
frase_espacios = frase.split(" ")
print(frase_espacios)

# Encontrar la posición de una subcadena dentro de la cadena
posicion = frase.find("programación")
print(posicion)

# Verificar si todos los caracteres de la cadena son dígitos
numero_texto = "23"
is_digit = numero_texto.isdigit()
print(is_digit)
