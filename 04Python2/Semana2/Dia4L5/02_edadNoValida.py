class EdadInvalidaError(Exception):
    def __init__(self, mensaje="La edad proporcionada no es válida."):
        super().__init__(mensaje)

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser un número negativo.")
    elif edad > 120:
        raise EdadInvalidaError("La edad proporcionada es demasiado alta.")

# Ejemplo de uso
try:
    edad = -5
    verificar_edad(edad)
except EdadInvalidaError as e:
    print("Error de edad:", e)
