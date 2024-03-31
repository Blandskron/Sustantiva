def division(a, b):
    try:
        resultado = a / b
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Ejemplo de uso
division(10, 0)
