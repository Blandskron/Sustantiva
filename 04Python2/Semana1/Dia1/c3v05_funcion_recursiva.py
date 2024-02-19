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


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
