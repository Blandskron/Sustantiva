import os

# Ruta y nombre original de la imagen
ruta_original = 'imagen.jpg'

# Nuevo nombre de la imagen
nuevo_nombre = 'nueva_imagen.jpg'

# Renombrar la imagen
try:
    os.rename(ruta_original, nuevo_nombre)
    print(f"La imagen '{ruta_original}' ha sido renombrada como '{nuevo_nombre}'.")
except FileNotFoundError:
    print(f"No se encontró la imagen '{ruta_original}'.")
except FileExistsError:
    print(f"Ya existe una imagen con el nombre '{nuevo_nombre}'.")
except Exception as e:
    print("Error al intentar renombrar la imagen:", e)
