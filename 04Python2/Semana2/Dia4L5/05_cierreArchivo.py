try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
finally:
    if 'archivo' in locals():
        archivo.close()
