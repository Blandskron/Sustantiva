# Imprime la cabecera de la tabla de conversión de Fahrenheit a Celsius
print("f  c")

# Itera sobre cada temperatura en el rango de 0 a 20 (inclusive)
for temp in range(21):
    # Imprime la temperatura en grados Fahrenheit y su equivalente en grados Celsius
    # Se convierte la temperatura de Fahrenheit a Celsius mediante la fórmula (Fahrenheit - 32) * 5/9
    print(temp, " ", int((temp-32)*5/9))
