import random

def jugar_ppt():
    opciones = ['piedra', 'papel', 'tijeras']
    
    # Solicitar al jugador que elija una opción
    print("Elige una opción: piedra, papel o tijeras")
    eleccion_jugador = input("Tu elección: ").lower()
    
    # Validar la elección del jugador
    if eleccion_jugador not in opciones:
        print("¡Opción no válida!")
        return
    
    # Generar la elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)
    
    # Mostrar las elecciones
    print("La computadora eligió:", eleccion_computadora)
    print("Tú elegiste:", eleccion_jugador)
    
    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:
        print("¡Empate!")
    elif (eleccion_jugador == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_jugador == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_jugador == 'tijeras' and eleccion_computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡La computadora gana!")

# Jugar al juego
jugar_ppt()
