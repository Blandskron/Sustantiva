try:
    # Abre el archivo en modo lectura
    with open('archivo.txt', 'r') as archivo:
        # Lee el contenido del archivo
        contenido = archivo.read()
        # Muestra el contenido en la consola
        print(contenido)
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
