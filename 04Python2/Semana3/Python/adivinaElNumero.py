def adivina_el_numero():
    import random

    print("Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intentos += 1
        entrada = input("Intenta adivinar el número: ")

        if not entrada.isdigit():
            print("Por favor ingresa un número válido.")
            continue

        numero_usuario = int(entrada)

        if numero_usuario < numero_secreto:
            print("Demasiado bajo.")
        elif numero_usuario > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"Felicidades! Has adivinado el número en {intentos} intentos.")
            break

adivina_el_numero()
