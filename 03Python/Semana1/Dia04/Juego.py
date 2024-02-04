import random  # Importa el módulo random para generar elecciones aleatorias

def jugar_ppt():
    opciones = ['piedra', 'papel', 'tijeras']  # Define las opciones posibles del juego

    # Solicitar al jugador que elija una opción
    print("Elige una opción: piedra, papel o tijeras")
    eleccion_jugador = input("Tu elección: ").lower()  # Convierte la entrada del jugador a minúsculas

    # Validar la elección del jugador
    if eleccion_jugador not in opciones:  # Verifica si la elección del jugador no está en las opciones válidas
        print("¡Opción no válida!")  # Muestra un mensaje de error
        return  # Sale de la función si la elección no es válida

    # Generar la elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)  # Elige aleatoriamente una opción de la lista opciones

    # Mostrar las elecciones
    print("La computadora eligió:", eleccion_computadora)  # Muestra la elección de la computadora
    print("Tú elegiste:", eleccion_jugador)  # Muestra la elección del jugador

    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:  # Si las elecciones son iguales
        print("¡Empate!")  # Muestra un mensaje de empate
    elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_jugador == 'tijeras' and eleccion_computadora == 'papel'):
        # Si el jugador gana según las reglas del juego
        print("¡Ganaste!")  # Muestra un mensaje de victoria del jugador
    else:  # Si no se cumple ninguna de las condiciones anteriores
        print("¡La computadora gana!")  # Muestra un mensaje de victoria de la computadora

# Jugar al juego
jugar_ppt()
