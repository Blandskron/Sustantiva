# Definición de variables con diferentes tipos de datos
nombre = "María"          # Cadena de caracteres
edad = 25                 # Entero
altura = 1.65             # Flotante
es_estudiante = True      # Booleano
colores_favoritos = ["azul", "verde", "morado"]  # Lista de colores favoritos
informacion_personal = {"nombre": "María", "edad": 25, "ciudad": "Madrid"}  # Diccionario de información personal

# Función para saludar
def saludar(nombre):
    print("¡Hola,", nombre, "! Bienvenido.")

# Función para calcular el promedio de una lista de números
def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

# Llamada a la función saludar
saludar(nombre)

# Imprimir información personal
print("Información personal:")
for clave, valor in informacion_personal.items():
    print(clave.capitalize() + ":", valor)

# Llamada a la función para calcular el promedio
numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(numeros)
print("El promedio de la lista de números es:", promedio)

# Estructura de control if-elif-else para tomar decisiones
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres mayor de edad y estás en edad laboral.")
else:
    print("Eres mayor de edad y estás en edad de jubilación.")

# Estructura de control while para repetir acciones mientras se cumpla una condición
contador = 0
while contador < 3:
    print("Iteración:", contador)
    contador += 1

# Estructura de control for para iterar sobre una secuencia de elementos
print("Colores favoritos:")
for color in colores_favoritos:
    print(color)
