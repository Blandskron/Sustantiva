def ejemplo(*args, **kwargs):
    print("Argumentos posicionales (args):", args)
    print("Argumentos de palabra clave (kwargs):", kwargs)

# Llamando a la función ejemplo con diferentes tipos de argumentos
ejemplo(1, 2, 3, nombre="Juan", edad=30)
