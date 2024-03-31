def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# Ejemplo de polimorfismo
operaciones = [sumar, restar, multiplicar]

a = 5
b = 3

for operacion in operaciones:
    print(operacion(a, b))
