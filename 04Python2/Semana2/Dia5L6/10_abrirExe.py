import os

nombre_archivo = 'programa.exe'

if os.path.exists(nombre_archivo):
    permisos = os.access(nombre_archivo, os.X_OK)  # Verifica si el archivo es ejecutable
    if permisos:
        print(f"El archivo '{nombre_archivo}' es ejecutable.")
    else:
        print(f"El archivo '{nombre_archivo}' no es ejecutable.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")
