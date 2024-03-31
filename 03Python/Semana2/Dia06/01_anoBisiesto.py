# Definición de una función llamada is_leap_year que determina si un año es bisiesto.
# Toma un argumento:
# - year: el año que se va a comprobar
def is_leap_year(year):
    # Comprueba si el año es un número entero positivo.
    # Si el año no es entero o es menor o igual a cero, no puede ser un año válido.
    if year % 1 != 0 or year <= 0:
        return False
    
    # Comprueba si el año es divisible por 4.
    if year % 4 == 0:
        # Si el año es divisible por 100, también se comprueba si es divisible por 400.
        # Si es divisible por 400, es un año bisiesto.
        if year % 100 == 0 and year % 400 == 0:
            return True
        # Si el año es divisible por 100 pero no por 400, no es un año bisiesto.
        if year % 100 == 0:
            return False
        # Si el año es divisible por 4 pero no por 100, es un año bisiesto.
        return True
    
    # Si el año no es divisible por 4, no es un año bisiesto.
    return False

# Llama a la función is_leap_year con el año 2000.
# La función devuelve True si el año es bisiesto, de lo contrario devuelve False.
response = is_leap_year(2000)

# Imprime la respuesta que indica si el año 2000 es bisiesto o no.
print(response)
