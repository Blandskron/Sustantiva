"""
Suceción de Fibonacci
0 1 1 2 3 5 8 13 21


Función recursiva

def funcion_recursiva():
    if condition:
        return
    return funcion_recursiva()

funcion_recursiva()


fibonacci(3)
n = 3   -> fibonacci(2) + fibonacci(1)
        -> fibonacci(1) + fibonacci(0) + fibonacci(1)
        -> 1 + 0 + 1 = 2
n = 2   -> fibonacci(1) + fibonacci(0)
n = 1   -> 1
n = 0   -> 0

"""
# Definición de la función de Fibonacci
def fibonacci(n):
    # Caso base: si n es 0 o 1, el número de Fibonacci es simplemente n
    if n <= 1:
        return n

    # Caso recursivo: el número de Fibonacci para n es la suma de los números
    # de Fibonacci para n-1 y n-2
    return fibonacci(n - 1) + fibonacci(n - 2)

# Imprime el número de Fibonacci para n=3
print(fibonacci(3))
