# Conversión de un número representado como cadena a un entero
numero_texto = "38"
numero_entero = int(numero_texto)
print(numero_entero)  # Imprime el número entero 38
print(type(numero_entero))  # Imprime el tipo de dato de numero_entero (int)

# Conversión de un número de punto flotante a un entero
numero_float = 0.5
numero_entero = int(numero_float)
print(numero_entero)  # Imprime el número entero 0 (solo se toma la parte entera del número float)
print(type(numero_entero))  # Imprime el tipo de dato de numero_entero (int)

# Conversión de una cadena que representa un número de punto flotante a un float
float_texto = "2.5"
numero_float = float(float_texto)
print(numero_float)  # Imprime el número flotante 2.5
print(type(numero_float))  # Imprime el tipo de dato de numero_float (float)

# Conversión de un entero a una cadena
numero_entero = 32
texto_entero = str(numero_entero)
print(texto_entero)  # Imprime la cadena "32"
print(type(texto_entero))  # Imprime el tipo de dato de texto_entero (str)

# Conversión de un número de punto flotante a una cadena
numero_float = 3.14
texto_float = str(numero_float)
print(texto_float)  # Imprime la cadena "3.14"
print(type(texto_float))  # Imprime el tipo de dato de texto_float (str)
