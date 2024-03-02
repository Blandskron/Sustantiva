def validar_edad(edad):
    if edad < 0:
        raise Exception("La edad no puede ser un número negativo.")

# Ejemplo de uso
try:
    validar_edad(-5)
except Exception as e:
    print("Error:", e)
