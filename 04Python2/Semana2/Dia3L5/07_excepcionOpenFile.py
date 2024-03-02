try:
    with open("archivo_que_no_existe.txt", "r") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print("Error: El archivo no existe o no se puede abrir.")
except IOError as e:
    print("Error de E/S:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
