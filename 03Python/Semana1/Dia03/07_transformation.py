# Definir una variable 'name' con el valor "Nicolas"
name = "Nicolas"
print(type(name))  # Imprimir el tipo de 'name', que es <class 'str'>

# Reasignar 'name' a un entero
name = 12
print(type(name))  # Imprimir el tipo de 'name', que ahora es <class 'int'>

# Reasignar 'name' a un booleano
name = True
print(type(name))  # Imprimir el tipo de 'name', que ahora es <class 'bool'>

# Concatenar cadenas de texto
print("Nicolas" + " Molina")  # Imprime "Nicolas Molina"
# Sumar enteros
print(10 + 20)  # Imprime 30
# Concatenar cadena de texto con un número como cadena
print("Nicolas" + "12")  # Imprime "Nicolas12"

# Definir una variable 'age' como entero
age = 12
# Concatenar una cadena de texto con una representación de cadena del entero
print("Mi edad es " + str(age))  # Imprime "Mi edad es 12"
# Utilizar f-strings para interpolar el valor de 'age'
print(f"Mi edad es {age}")  # Imprime "Mi edad es 12"

# Solicitar al usuario que ingrese su edad y convertir la entrada a entero
age = input('Escribe tu edad => ')
print(type(age))  # Imprimir el tipo de 'age', que es <class 'str'>
age = int(age)    # Convertir la cadena a entero
age += 10         # Sumar 10 a 'age'
print(f'Tu edad en 10 años será {age}')  # Imprimir la edad aumentada en 10 años
