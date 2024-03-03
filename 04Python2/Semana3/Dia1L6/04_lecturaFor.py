try:
    # Abre el archivo en modo lectura
    with open('archivo.txt', 'r') as archivo:
        print("Contenido del archivo línea por línea:")
        
        # Itera sobre cada línea del archivo
        for linea in archivo:
            # Imprime la línea actual
            print(linea.strip())  # strip() elimina los caracteres de nueva línea al final
except FileNotFoundError:
    print("El archivo no se ha encontrado.")
except Exception as e:
    print("Error:", e)
