try:
    # Abre el archivo en modo escritura
    with open('archivo.txt', 'w') as archivo:
        # Escribe en el archivo
        archivo.write("Hola, mundo!")
        print("Se ha escrito en el archivo correctamente.")
except Exception as e:
    print("Error:", e)
