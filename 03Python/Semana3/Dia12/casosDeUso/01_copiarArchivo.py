# Importamos el módulo shutil, que proporciona operaciones de alto nivel para trabajar con archivos y directorios.
import shutil

# Definimos una función llamada copiar_archivo que intentará copiar un archivo de una ubicación a otra.
def copiar_archivo(ubicacion_actual, ubicacion_nueva):
    try:
        # Intentamos copiar el archivo desde la ubicación actual a la nueva ubicación utilizando la función shutil.copy().
        shutil.copy(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        # En caso de que ocurra una excepción durante la copia del archivo, capturamos el error y lo imprimimos.
        print(e)

# Llamamos a la función copiar_archivo con las rutas de ubicación del archivo actual y la nueva ubicación como argumentos.
copiar_archivo("archivos_ejemplo/archivo.txt", "archivo.txt")
