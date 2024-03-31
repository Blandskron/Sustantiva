import os

# Ruta y nombre original del archivo
ruta_original = 'archivo.txt'

# Nuevo nombre del archivo
nuevo_nombre = 'nuevo_archivo.txt'

# Renombrar el archivo
try:
    os.rename(ruta_original, nuevo_nombre)
    print(f"El archivo '{ruta_original}' ha sido renombrado como '{nuevo_nombre}'.")
except FileNotFoundError:
    print(f"No se encontró el archivo '{ruta_original}'.")
except FileExistsError:
    print(f"Ya existe un archivo con el nombre '{nuevo_nombre}'.")
except Exception as e:
    print("Error al intentar renombrar el archivo:", e)
