# Asigna un valor inicial a la temperatura en grados Fahrenheit
temp = 32

# Imprime la cabecera de la tabla de conversión de Fahrenheit a Celsius
print("f   c")

# Mientras la temperatura sea menor que 73, se ejecuta el bucle
while temp < 73:
    # Imprime la temperatura en grados Fahrenheit y su equivalente en grados Celsius
    # Se convierte la temperatura de Fahrenheit a Celsius mediante la fórmula (Fahrenheit - 32) * 5/9
    print(temp, " ", int((temp-32)*5/9))
    
    # Incrementa la temperatura en 1 grado Fahrenheit para la próxima iteración del bucle
    temp = temp + 1
