try:
    # Modo de apertura para lectura ('r')
    with open('archivo.txt', 'r') as archivo_lectura:
        contenido_lectura = archivo_lectura.read()
        print("Modo de lectura ('r'):")
        print(contenido_lectura)

    # Modo de apertura para escritura ('w')
    with open('archivo_nuevo.txt', 'w') as archivo_escritura:
        archivo_escritura.write("Este es un archivo de texto nuevo.")
        print("\nModo de escritura ('w'): Se ha escrito en el archivo.")

    # Modo de apertura para anexar ('a')
    with open('archivo.txt', 'a') as archivo_anexar:
        archivo_anexar.write("\nEsta línea se añadirá al final del archivo.")
        print("\nModo de anexar ('a'): Se ha añadido contenido al archivo.")

except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
