# Verificación de una condición verdadera
if True:
    print('debería ejecutarse')  # Como la condición es verdadera, este mensaje se imprimirá

# Verificación de una condición falsa
if False:
    print('nunca se ejecuta')  # Esta línea de código no se ejecutará porque la condición es falsa

# Caso uno: Determinación de la mascota favorita
pet = input('¿Cuál es tu mascota favorita? ')  # Solicita al usuario que ingrese su mascota favorita

# Utiliza una serie de condicionales para determinar la respuesta en función de la mascota ingresada
if pet == 'perro':
    print('¡Genial, tienes buen gusto!')  # Si la mascota es 'perro'
elif pet == 'gato':
    print('Espero que tengas suerte')     # Si la mascota es 'gato'
elif pet == 'pez':
    print('Eres lo máximo')                # Si la mascota es 'pez'
else:
    print('No tienes ninguna mascota interesante')  # Si la mascota no coincide con las anteriores

# Caso dos: Verificación del stock
stock = int(input('Digita el stock => '))  # Solicita al usuario que ingrese el stock como un número entero

# Utiliza una declaración condicional para verificar si el stock está dentro de un rango específico
if stock >= 100 and stock <= 1000:
    print('El stock es correcto')     # Si el stock está dentro del rango especificado
else:
    print('El stock es incorrecto')   # Si el stock no está dentro del rango especificado

# Caso tres: Verificación de si un número es par o impar
number = int(input('Ingrese un número => '))  # Solicita al usuario que ingrese un número

# Calcula el residuo de la división del número por 2 para determinar si es par o impar
result = number % 2

# Utiliza una declaración condicional para determinar si el número es par o impar
if result == 0:
    print('Es par')   # Si el residuo es cero, el número es par
else:
    print('Es impar')  # Si el residuo no es cero, el número es impar
