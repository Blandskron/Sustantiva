# Definición de la función ejemplo() que acepta un número variable de argumentos posicionales y argumentos de palabra clave
def ejemplo(*args, **kwargs):
    # Imprime los argumentos posicionales (args)
    print("Argumentos posicionales (args):", args)
    # Imprime los argumentos de palabra clave (kwargs)
    print("Argumentos de palabra clave (kwargs):", kwargs)

# Llamada a la función ejemplo() con diferentes tipos de argumentos
ejemplo(1, 2, 3, nombre="Juan", edad=30)
