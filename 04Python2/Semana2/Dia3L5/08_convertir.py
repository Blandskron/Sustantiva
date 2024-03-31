def convertir_a_entero(cadena):
    try:
        numero = int(cadena)
        print("Número convertido:", numero)
    except ValueError:
        print("Error: La cadena no es un número entero válido.")

# Ejemplo de uso
convertir_a_entero("123")
convertir_a_entero("abc")
