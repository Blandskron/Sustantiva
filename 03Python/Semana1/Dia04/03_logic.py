# Operador AND
print('AND')
print('True and True =>', True and True)    # True
print('True and False =>', True and False)  # False
print('False and True =>', False and True)  # False
print('False and False =>', False and False)  # False

# Ejemplos de uso de AND con expresiones
print(10 > 5 and 5 < 10)   # True
print(10 > 5 and 5 > 10)   # False

# Verificar si el valor de stock está entre 100 y 1000
stock = input('Ingrese el numero de stock => ')
stock = int(stock)
print(stock >= 100 and stock <= 1000)

# Operador OR
print('OR')
print('True or True =>', True or True)      # True
print('True or False =>', True or False)     # True
print('False or True =>', False or True)     # True
print('False or False =>', False or False)   # False

# Verificar si el rol es 'admin' o 'seller'
role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')
