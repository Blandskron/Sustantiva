import importlib


def importar_modulo(ruta_modulo):
    try:
        modulo = importlib.import_module(ruta_modulo)
        print(f"El modulo {ruta_modulo} si existe.")
        return modulo
    except ModuleNotFoundError:
        print(f"No se encontró el módulo {ruta_modulo}")
        return


def invocar_funcion(ruta_modulo, nombre_funcion, *args, **kwargs):

    modulo = importar_modulo(ruta_modulo)

    if nombre_funcion not in dir(modulo):
        print("La función no existe en el módulo")
        return

    funcion = getattr(modulo, nombre_funcion)
    if not hasattr(funcion, "__call__"):
        print("No es posible invocar la función")
        return

    funcion(*args, **kwargs)


ruta_modulo = "archivos_ejemplo.ejemplo"
nombre_funcion = "funcion_ejemplo"
invocar_funcion(ruta_modulo, nombre_funcion)
