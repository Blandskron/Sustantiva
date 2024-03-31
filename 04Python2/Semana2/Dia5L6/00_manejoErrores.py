class ManejoArchivos:
    def __init__(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                print("Contenido del archivo:", contenido)
        except FileNotFoundError:
            print("Error: El archivo no existe.")
        except PermissionError:
            print("Error: Permiso denegado para acceder al archivo.")
        except ValueError:
            print("Error: Problema al leer el contenido del archivo.")

# Ejemplo de uso
archivo = "datos.txt"
manejo_archivos = ManejoArchivos(archivo)
