def juego_trivia_ciencia():
    preguntas = {
        "¿Cuál es el elemento químico más ligero?": {
            "opciones": ["Hidrógeno", "Oxígeno", "Carbono", "Helio"],
            "respuesta": "Hidrógeno"
        },
        "¿Cuál es el planeta más grande del Sistema Solar?": {
            "opciones": ["Júpiter", "Saturno", "Urano", "Neptuno"],
            "respuesta": "Júpiter"
        },
        "¿Qué tipo de animal es una ballena?": {
            "opciones": ["Pez", "Mamífero", "Reptil", "Anfibio"],
            "respuesta": "Mamífero"
        },
        # Se pueden añadir más preguntas aquí
    }

    correctas = 0

    print("Bienvenido al Juego de Trivia Científica\n")

    for pregunta, datos in preguntas.items():
        print(pregunta)
        for i, opcion in enumerate(datos["opciones"], 1):
            print(f"{i}. {opcion}")
        
        respuesta_usuario = input("Ingresa el número de tu respuesta: ")

        if datos["opciones"][int(respuesta_usuario) - 1] == datos["respuesta"]:
            print("¡Correcto!\n")
            correctas += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {datos['respuesta']}\n")

    print(f"Juego terminado. Tu puntuación es {correctas}/{len(preguntas)}.")


juego_trivia_ciencia()
