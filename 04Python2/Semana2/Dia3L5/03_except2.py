def convertir_entero(cadena):
    try:
        entero = int(cadena)
        print("El entero convertido es:", entero)
    except ValueError:
        print("Error: No se puede convertir la cadena a entero.")

# Ejemplo de uso
convertir_entero("abc")
