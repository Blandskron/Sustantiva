# Operador NOT
print(not True)    # False
print(not False)   # True

# Operador AND con NOT
print('NOT AND')
print('not True and True =>', not (True and True))      # False
print('not True and False =>', not (True and False))    # True
print('not False and True =>', not (False and True))    # True
print('not False and False =>', not (False and False))  # True

# Verificar si el valor de stock está fuera del rango entre 100 y 1000
stock = input('Ingrese el numero de stock => ')
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))
