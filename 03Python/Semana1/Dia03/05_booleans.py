# Definimos una variable llamada is_single y le asignamos el valor True
is_single = True

# Imprimimos el tipo de dato de la variable is_single
print(type(is_single))  # Imprime <class 'bool'>, indicando que is_single es de tipo booleano

# Reasignamos el valor de la variable is_single a False
is_single = False

# Imprimimos el valor de la variable is_single
print(is_single)  # Imprime False

# Utilizamos el operador 'not' para negar el valor True
print(not True)  # Imprime False

# Utilizamos el operador 'not' para negar el valor False
print(not False)  # Imprime True

# Negamos el valor de la variable is_single y lo asignamos de nuevo a is_single
is_single = not is_single

# Imprimimos el valor de la variable is_single después de la negación
print(is_single)  # Imprime True
