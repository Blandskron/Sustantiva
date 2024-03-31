class Calculadora:
    def sumar(self, a, b=None):
        if b is None:
            return a
        else:
            return a + b

# Crear instancia de la calculadora
calc = Calculadora()

# Ejemplos de uso de la calculadora
print(calc.sumar(2, 3))  # Imprime: 5
print(calc.sumar(2))      # Imprime: 2
