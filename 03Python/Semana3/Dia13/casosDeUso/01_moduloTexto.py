# Importamos el módulo importlib, que nos permite trabajar con la importación dinámica de módulos en Python.
import importlib

# Definimos una función llamada importar_modulo que importa un módulo dado su nombre o ruta.
def importar_modulo(ruta_modulo):
    try:
        # Intentamos importar el módulo utilizando importlib.import_module().
        modulo = importlib.import_module(ruta_modulo)
        # Si el módulo se importa con éxito, imprimimos un mensaje indicando que el módulo existe y lo retornamos.
        print(f"El modulo {ruta_modulo} si existe.")
        return modulo
    except ModuleNotFoundError:
        # Si el módulo no se encuentra, capturamos la excepción ModuleNotFoundError e imprimimos un mensaje apropiado.
        print(f"No se encontró el módulo {ruta_modulo}")
        return None

# Definimos una función llamada invocar_funcion que invoca una función de un módulo importado dinámicamente.
def invocar_funcion(ruta_modulo, nombre_funcion, *args, **kwargs):
    # Importamos el módulo especificado.
    modulo = importar_modulo(ruta_modulo)

    # Verificamos si el módulo se importó con éxito.
    if modulo is None:
        return

    # Verificamos si la función existe en el módulo.
    if nombre_funcion not in dir(modulo):
        print("La función no existe en el módulo")
        return

    # Obtenemos la referencia a la función.
    funcion = getattr(modulo, nombre_funcion)
    
    # Verificamos si la referencia obtenida es una función invocable.
    if not hasattr(funcion, "__call__"):
        print("No es posible invocar la función")
        return

    # Invocamos la función con los argumentos y palabras clave proporcionados.
    funcion(*args, **kwargs)


# Definimos la ruta del módulo y el nombre de la función que queremos invocar.
ruta_modulo = "archivos_ejemplo.ejemplo"
nombre_funcion = "funcion_ejemplo"

# Invocamos la función con los argumentos proporcionados.
invocar_funcion(ruta_modulo, nombre_funcion)
