def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    else:
        return a / b

# Ejemplo de uso
try:
    resultado = dividir(10, 0)
    print("Resultado de la división:", resultado)
except ValueError as e:
    print("Error:", e)
