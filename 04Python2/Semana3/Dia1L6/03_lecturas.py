try:
    # Modo de lectura normal 'r'
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
        print("Modo de lectura normal ('r'):")
        print(contenido)

    # Modo de lectura binaria 'rb'
    with open('archivo.bin', 'rb') as archivo_binario:
        contenido_binario = archivo_binario.read()
        print("\nModo de lectura binaria ('rb'):")
        print(contenido_binario)

    # Modo de lectura y escritura 'r+'
    with open('archivo_rw.txt', 'r+') as archivo_rw:
        contenido_rw = archivo_rw.read()
        archivo_rw.write("Añadiendo texto en modo lectura/escritura.")
        archivo_rw.seek(0)  # Volvemos al principio del archivo
        print("\nModo de lectura/escritura ('r+'):")
        print(archivo_rw.read())

    # Modo de lectura binaria y escritura 'rb+'
    with open('archivo_binario_rw.bin', 'rb+') as archivo_binario_rw:
        contenido_binario_rw = archivo_binario_rw.read()
        archivo_binario_rw.write(b'A\xFF\x00\x55')  # Escribiendo bytes binarios
        archivo_binario_rw.seek(0)  # Volvemos al principio del archivo
        print("\nModo de lectura/escritura binaria ('rb+'):")
        print(archivo_binario_rw.read())

    # Modo de lectura y escritura con creación 'w+'
    with open('archivo_nuevo.txt', 'w+') as archivo_nuevo:
        archivo_nuevo.write("Este es un archivo nuevo.")
        archivo_nuevo.seek(0)  # Volvemos al principio del archivo
        print("\nModo de lectura/escritura con creación ('w+'):")
        print(archivo_nuevo.read())

    # Modo de lectura y escritura binaria con creación 'wb+'
    with open('archivo_nuevo_binario.bin', 'wb+') as archivo_nuevo_binario:
        archivo_nuevo_binario.write(b'\x00\xFF\xAA\x55')
        archivo_nuevo_binario.seek(0)  # Volvemos al principio del archivo
        print("\nModo de lectura/escritura binaria con creación ('wb+'):")
        print(archivo_nuevo_binario.read())

except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
