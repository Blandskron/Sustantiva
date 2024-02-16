# Importamos el módulo os, que proporciona funciones para interactuar con el sistema operativo.
import os

# Definimos una función llamada borrar_archivo que intentará eliminar un archivo en la ruta especificada.
def borrar_archivo(ruta_archivo):
    try:
        # Intentamos eliminar el archivo especificado por la ruta utilizando la función os.remove().
        os.remove(ruta_archivo)
    except Exception as e:
        # En caso de que ocurra una excepción durante la eliminación del archivo, capturamos el error y lo imprimimos.
        print(e)

# Llamamos a la función borrar_archivo con la ruta del archivo que queremos eliminar como argumento.
borrar_archivo("archivos_ejemplo/archivo_borrar.txt")
