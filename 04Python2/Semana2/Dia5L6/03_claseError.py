class MiError(Exception):
    def __init__(self, mensaje="Ha ocurrido un error."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Ejemplo de uso
def dividir(a, b):
    if b == 0:
        raise MiError("No se puede dividir entre cero.")
    else:
        return a / b

# Ejemplo de manejo de la excepción personalizada
try:
    resultado = dividir(10, 0)
    print("Resultado de la división:", resultado)
except MiError as e:
    print("Se produjo un error personalizado:", e)
