# Asignamos la cadena de texto '10' a la variable number
number = '10'

# Imprimimos el valor de la variable number, que es una cadena de texto
print(number)

# Convertimos la cadena de texto '10' a un entero utilizando la función int() y luego verificamos si es par o impar
if int(number) % 2 == 0:
    # Si el número convertido a entero es divisible por 2 (es par), imprimimos 'Es par'
    print('Es par')
else:
    # Si el número convertido a entero no es divisible por 2 (es impar), imprimimos 'Es impar'
    print('Es impar')
