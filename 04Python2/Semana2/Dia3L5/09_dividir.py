def dividir(a, b):
    try:
        resultado = a / b
        print("Resultado de la división:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Ejemplo de uso
dividir(10, 2)
dividir(5, 0)
