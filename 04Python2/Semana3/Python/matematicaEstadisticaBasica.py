import statistics

# Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# 1. Suma
suma = sum(numeros)
print(f"Suma: La suma de {numeros} es {suma}")

# 2. Promedio (media)
promedio = statistics.mean(numeros)
print(f"Promedio: El promedio de {numeros} es {promedio}")

# 3. Mediana
mediana = statistics.median(numeros)
print(f"Mediana: La mediana de {numeros} es {mediana}")

# 4. Moda
moda = statistics.mode(numeros)
print(f"Moda: La moda de {numeros} es {moda}")

# 5. Desviación estándar
desviacion_estandar = statistics.stdev(numeros)
print(f"Desviación Estándar: La desviación estándar de {numeros} es {desviacion_estandar}")

# 6. Varianza
varianza = statistics.variance(numeros)
print(f"Varianza: La varianza de {numeros} es {varianza}")
