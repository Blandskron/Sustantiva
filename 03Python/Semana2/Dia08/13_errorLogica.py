# Programa para calcular la suma de los números del 1 al 10

suma = 0
for i in range(1, 11):
    suma = suma + i
print("La suma de los números del 1 al 10 es: ", suma)


# Programa para calcular el promedio de una lista de números

numeros = [10, 8, 9, 7, 6]
suma = 0
for num in numeros:
    suma += num
promedio = suma / len(numeros)
print("El promedio de los números es: ", promedio)
