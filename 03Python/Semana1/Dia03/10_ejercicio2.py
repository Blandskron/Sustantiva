try:
    # Solicitar al usuario ingresar un número
    numero = int(input("Ingresa un número para generar la tabla de multiplicar: "))

    # Inicializar una lista para almacenar la tabla de multiplicar
    tabla_multiplicar = []

    # Generar la tabla de multiplicar hasta 10 usando un ciclo for
    for i in range(1, 11):
        resultado = numero * i
        tabla_multiplicar.append(resultado)

    # Imprimir la tabla de multiplicar
    print(f"La tabla de multiplicar del {numero} es: {tabla_multiplicar}")

except ValueError:
    # Manejar la excepción si el usuario no ingresa un número entero
    print("Por favor, ingresa un número entero.")
