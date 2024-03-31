import os

nombre_archivo = 'imagen1.jpg'

if os.path.exists(nombre_archivo):
    tamaño = os.path.getsize(nombre_archivo)  # Tamaño del archivo en bytes
    tipo = nombre_archivo.split('.')[-1]  # Obtiene la extensión del archivo
    print(f"El archivo '{nombre_archivo}' es de tipo '{tipo}' y tiene un tamaño de {tamaño} bytes.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")
