# Define una cadena de texto
text = 'Ella sabe programar en Python'

# Verifica si la subcadena 'JavaScript' está presente en la cadena de texto
print('JavaScript' in text)

# Verifica si la subcadena 'Python' está presente en la cadena de texto
print('Python' in text)

# Verifica si la subcadena 'JS' está presente en la cadena de texto
# Este bloque no se ejecutará porque 'JS' no está presente en 'text'
if 'JS' in text:
    print('Elegiste bien!!')
else:
    print('También elegiste bien')

# Calcula la longitud de la cadena de texto
size = len(text)
print(size)

# Imprime la cadena de texto original
print(text)

# Imprime la cadena de texto en mayúsculas
print(text.upper())

# Imprime la cadena de texto en minúsculas
print(text.lower())

# Cuenta cuántas veces aparece la letra 'a' en la cadena de texto
print(text.count('a'))

# Intercambia las mayúsculas y minúsculas en la cadena de texto
print(text.swapcase())

# Verifica si la cadena de texto comienza con 'Ella'
print(text.startswith('Ella'))

# Verifica si la cadena de texto termina con 'Javascript'
print(text.endswith('Javascript'))

# Reemplaza todas las apariciones de 'Python' con 'Go' en la cadena de texto
print(text.replace('Python', 'Go'))

# Define una nueva cadena de texto
text_2 = 'este es un titulo'

# Imprime la cadena de texto original
print(text_2)

# Capitaliza la primera letra de la cadena de texto
print(text_2.capitalize())

# Convierte la cadena de texto en un título (capitaliza la primera letra de cada palabra)
print(text_2.title())

# Verifica si todos los caracteres de la cadena de texto son dígitos
print(text_2.isdigit())

# Verifica si todos los caracteres de la cadena de texto son dígitos (en este caso, son dígitos)
print("398".isdigit())

# Verifica si todos los caracteres de la cadena de texto son dígitos (en este caso, no son dígitos)
print("hola".isdigit())
