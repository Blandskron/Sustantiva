class OperacionesMatematicas:
    def division(self, a, b):
        try:
            resultado = a / b
            print("Resultado de la división:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        except TypeError:
            print("Error: Tipo de dato no compatible para la operación.")
        except NameError:
            print("Error: Nombre de variable no definido.")

# Ejemplo de uso
operaciones = OperacionesMatematicas()
operaciones.division(10, 0)  # Genera una excepción ZeroDivisionError
operaciones.division(10, 'a')  # Genera una excepción TypeError
