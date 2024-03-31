def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No es posible dividir por cero.")
    return a / b

def main():
    try:
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        else:
            raise ValueError("Operación no válida.")

        print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
