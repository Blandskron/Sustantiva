import os

# Ruta y nombre original del archivo binario
ruta_original = 'datos.bin'

# Nuevo nombre del archivo binario
nuevo_nombre = 'nuevos_datos.bin'

# Renombrar el archivo binario
try:
    os.rename(ruta_original, nuevo_nombre)
    print(f"El archivo binario '{ruta_original}' ha sido renombrado como '{nuevo_nombre}'.")
except FileNotFoundError:
    print(f"No se encontró el archivo binario '{ruta_original}'.")
except FileExistsError:
    print(f"Ya existe un archivo binario con el nombre '{nuevo_nombre}'.")
except Exception as e:
    print("Error al intentar renombrar el archivo binario:", e)
