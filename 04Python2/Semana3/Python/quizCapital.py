def quiz_capitales():
    capitales = {
        "España": "Madrid",
        "Francia": "París",
        "Italia": "Roma",
        "Alemania": "Berlín",
        "Portugal": "Lisboa",
        # Se pueden añadir más países y capitales aquí
    }

    correctas = 0
    incorrectas = 0

    print("Bienvenido al Quiz de Capitales del Mundo")
    print("Escribe 'salir' para terminar el juego.\n")

    for pais, capital in capitales.items():
        respuesta = input(f"¿Cuál es la capital de {pais}? ").capitalize()

        if respuesta.lower() == 'salir':
            break

        if respuesta == capital:
            correctas += 1
            print("¡Correcto!")
        else:
            incorrectas += 1
            print(f"Incorrecto. La capital de {pais} es {capital}.")

    print("\nJuego terminado.")
    print(f"Respuestas correctas: {correctas}")
    print(f"Respuestas incorrectas: {incorrectas}")


quiz_capitales()
