# Definir una tupla con los nombres de los meses
nombres_meses = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)

while True:
    try:
        # Solicitar al usuario ingresar un número
        numero = int(input("Ingresa un número del 1 al 12 (o 0 para salir): "))

        # Salir del bucle si el usuario ingresa 0
        if numero == 0:
            print("¡Hasta luego!")
            break

        # Validar que el número esté en el rango del 1 al 12
        if 1 <= numero <= 12:
            # Imprimir el nombre del mes correspondiente
            print(f"El mes correspondiente al número {numero} es {nombres_meses[numero - 1]}.")
        else:
            # Indicar al usuario que solo se aceptan números del 1 al 12
            print("Por favor, ingresa un número válido del 1 al 12.")

    except ValueError:
        # Manejar la excepción si el usuario ingresa algo que no es un número entero
        print("Por favor, ingresa un número entero.")

# Fin del programa
