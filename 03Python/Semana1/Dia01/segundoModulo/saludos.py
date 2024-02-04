# Definición de la función de saludo con personalización
def saludar(nombre):
    """
    Esta función recibe un nombre como argumento
    y devuelve un saludo personalizado.
    """
    # Creamos un mensaje personalizado utilizando f-strings, donde {nombre} es el argumento proporcionado.
    mensaje = f"¡Hola, {nombre}! Bienvenido al mundo de los saludos en Python."
    
    # Imprimimos el mensaje en la consola.
    print(mensaje)
