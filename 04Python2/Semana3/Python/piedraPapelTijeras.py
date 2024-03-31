import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    # El jugador elige su opción
    eleccion_jugador = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion_jugador not in opciones:
        print("Opción inválida. Por favor elige piedra, papel o tijeras.")
        eleccion_jugador = input("Elige piedra, papel o tijeras: ").lower()

    # La computadora elige su opción
    eleccion_computadora = random.choice(opciones)
    print(f"Tu elección: {eleccion_jugador}")
    print(f"Elección de la computadora: {eleccion_computadora}")

    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:
        print("Es un empate!")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_jugador == "tijeras" and eleccion_computadora == "papel"):
        print("Ganaste!")
    else:
        print("Perdiste!")

# Para jugar, simplemente llama a la función
jugar_piedra_papel_tijeras()
