# Importamos el módulo shutil, que proporciona operaciones de alto nivel para trabajar con archivos y directorios.
import shutil

# Definimos una función llamada mover_archivo que moverá un archivo de una ubicación a otra.
def mover_archivo(ubicacion_actual, ubicacion_nueva):
    try:
        # Intentamos mover el archivo desde la ubicación actual a la nueva ubicación utilizando la función shutil.move().
        shutil.move(ubicacion_actual, ubicacion_nueva)
    except Exception as e:
        # En caso de que ocurra una excepción durante el movimiento del archivo, capturamos el error y lo imprimimos.
        print(e)

# Llamamos a la función mover_archivo con las rutas de ubicación del archivo actual y la nueva ubicación como argumentos.
mover_archivo("archivos_ejemplo/archivo.txt", "archivo.txt")
