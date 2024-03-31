import os
import time

nombre_archivo = 'texto.txt'

if os.path.exists(nombre_archivo):
    fecha_creacion = time.ctime(os.path.getctime(nombre_archivo))  # Fecha de creación del archivo
    fecha_modificacion = time.ctime(os.path.getmtime(nombre_archivo))  # Fecha de modificación del archivo
    print(f"El archivo '{nombre_archivo}' fue creado el {fecha_creacion} y modificado por última vez el {fecha_modificacion}.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")
