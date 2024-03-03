try:
    # Modo de lectura
    with open('archivo.txt', 'r') as archivo_lectura:
        contenido = archivo_lectura.read()
        print("Contenido del archivo:", contenido)

    # Modo de escritura
    with open('archivo.txt', 'w') as archivo_escritura:
        archivo_escritura.write("Este es un archivo de texto.")

    # Modo de anexar
    with open('archivo.txt', 'a') as archivo_anexar:
        archivo_anexar.write("\nEsta línea se agrega al final del archivo.")

except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
