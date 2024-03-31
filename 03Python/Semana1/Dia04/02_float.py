x = 3.3
print(x)  # Imprime el valor de x, que es 3.3
y = 1.1 + 2.2
print(y)  # Imprime el valor de y, que es 3.3000000000000003 (precisión de punto flotante)
print(x == y)  # Compara x e y, imprime False debido a la precisión de punto flotante

# Formateo de y como cadena con 2 dígitos significativos
y_str = format(y, ".2g")
print('str =>', y_str)  # Imprime la representación en cadena de y con 2 dígitos significativos
# Compara la cadena formateada de y con la cadena de x
print(y_str == str(x))  # Imprime True porque la cadena formateada es "3.3"

print('*' * 10)

print(y, x)  # Imprime los valores de y y x

# Tolerancia para comparar la diferencia entre x e y
tolerance = 0.00001
# Compara si la diferencia entre x e y es menor que la tolerancia
print(abs(x - y) < tolerance)  # Imprime True, la diferencia es menor que la tolerancia
