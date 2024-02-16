# Importamos el módulo importlib, que nos permite trabajar con la importación dinámica de módulos en Python.
import importlib

# Definimos una función llamada validar_modulo que intenta importar un módulo dado su nombre o ruta.
def validar_modulo(ruta_modulo):
    try:
        # Intentamos importar el módulo utilizando importlib.import_module().
        modulo = importlib.import_module(ruta_modulo)
        
        # Si el módulo se importa con éxito, imprimimos un mensaje indicando que el módulo existe y mostramos información sobre él.
        print(f"El modulo {ruta_modulo} si existe.")
        print(modulo)
    except ModuleNotFoundError:
        # Si el módulo no se encuentra, capturamos la excepción ModuleNotFoundError e imprimimos un mensaje apropiado.
        print(f"No se encontró el módulo {ruta_modulo}")

# Definimos la ruta del módulo que queremos validar.
ruta_modulo = "c2v07_copiar_archivoo"
# Llamamos a la función validar_modulo con la ruta del módulo como argumento.
validar_modulo(ruta_modulo=ruta_modulo)
