import importlib


def validar_modulo(ruta_modulo):
    try:
        modulo = importlib.import_module(ruta_modulo)
        print(f"El modulo {ruta_modulo} si existe.")
        print(modulo)
    except ModuleNotFoundError:
        print(f"No se encontró el módulo {ruta_modulo}")


ruta_modulo = "c2v07_copiar_archivoo"
validar_modulo(ruta_modulo=ruta_modulo)
