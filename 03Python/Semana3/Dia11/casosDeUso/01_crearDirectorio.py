# Importamos el módulo os, que proporciona funciones para interactuar con el sistema operativo.
import os

# Definimos una función llamada crear_directorio_vacio que intentará crear un directorio vacío en la ruta especificada.
def crear_directorio_vacio(ruta_directorio):
    try:
        # Intentamos crear un nuevo directorio en la ruta especificada utilizando la función os.mkdir().
        os.mkdir(ruta_directorio)
    except OSError as e:
        # En caso de que ocurra un error al intentar crear el directorio, capturamos la excepción y la imprimimos.
        print(e)

# Llamamos a la función crear_directorio_vacio con la ruta del directorio que queremos crear como argumento.
crear_directorio_vacio("directorio_vacio")
