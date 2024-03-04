# Ejemplo de manipulaciones de cadenas de caracteres en Python

# Definimos una cadena de ejemplo
cadena = "Hola, mundo!"

# 1. Longitud de la cadena
longitud = len(cadena)
print(f"Longitud de la cadena: '{cadena}' es {longitud}")

# 2. Concatenación de cadenas
cadena2 = " ¿Cómo estás?"
concatenacion = cadena + cadena2
print(f"Concatenación: '{cadena}' + '{cadena2}' = '{concatenacion}'")

# 3. Convertir a mayúsculas y minúsculas
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(f"Mayúsculas: '{cadena}' -> '{mayusculas}'")
print(f"Minúsculas: '{cadena}' -> '{minusculas}'")

# 4. Reemplazo de subcadena
reemplazo = cadena.replace("mundo", "Python")
print(f"Reemplazo: '{cadena}' -> '{reemplazo}'")

# 5. División de cadenas
dividido = cadena.split(", ")
print(f"División: '{cadena}' -> {dividido}")

# 6. Búsqueda de subcadenas
subcadena = "mundo"
posicion = cadena.find(subcadena)
print(f"Búsqueda: La subcadena '{subcadena}' se encuentra en la posición {posicion} en '{cadena}'")
