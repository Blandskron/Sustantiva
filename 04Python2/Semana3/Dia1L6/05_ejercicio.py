def abrir_archivo():
    global archivo
    try:
        archivo = open('datos.txt', 'a+')
        print("Archivo abierto correctamente.")
    except Exception as e:
        print("Error al abrir el archivo:", e)

def cerrar_archivo():
    global archivo
    try:
        archivo.close()
        print("Archivo cerrado correctamente.")
    except Exception as e:
        print("Error al cerrar el archivo:", e)

def mostrar_contenido():
    global archivo
    try:
        archivo.seek(0)
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except Exception as e:
        print("Error al mostrar el contenido del archivo:", e)

def escribir_tabla_multiplicar():
    global archivo
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    if 1 <= numero <= 10:
        try:
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")
            print(f"Se ha guardado la tabla de multiplicar del {numero} en el archivo.")
        except Exception as e:
            print("Error al escribir en el archivo:", e)
    else:
        print("El número ingresado está fuera del rango permitido.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Abrir archivo")
        print("2. Cerrar archivo")
        print("3. Mostrar contenido del archivo")
        print("4. Escribir tabla de multiplicar")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            abrir_archivo()
        elif opcion == '2':
            cerrar_archivo()
        elif opcion == '3':
            mostrar_contenido()
        elif opcion == '4':
            escribir_tabla_multiplicar()
        elif opcion == '5':
            cerrar_archivo()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamar a la función para ejecutar el programa
menu()
