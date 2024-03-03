try:
    # Abre el archivo en modo lectura
    with open('archivo.txt', 'r') as archivo:
        # Lee y muestra cada línea del archivo
        for linea in archivo:
            print(linea.strip())  # strip() elimina los caracteres de nueva línea al final
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
