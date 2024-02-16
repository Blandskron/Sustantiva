import os


def crear_directorio_vacio(ruta_directorio):

    try:
        os.mkdir(ruta_directorio)
    except OSError as e:
        print(e)


crear_directorio_vacio("directorio_vacio")
