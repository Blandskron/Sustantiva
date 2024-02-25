import random

class JuegoAdivinanza:
    def __init__(self):
        self.palabras = ['python', 'computadora', 'programacion', 'tecnologia', 'inteligencia']
        self.palabra_secreta = random.choice(self.palabras)
        self.intentos = 5
        self.letras_adivinadas = ['_'] * len(self.palabra_secreta)

    def adivinar_letra(self, letra):
        aciertos = 0
        for i, l in enumerate(self.palabra_secreta):
            if l == letra:
                self.letras_adivinadas[i] = letra
                aciertos += 1
        if aciertos == 0:
            self.intentos -= 1

    def jugar(self):
        print("¡Bienvenido al juego de adivinanzas!")
        while '_' in self.letras_adivinadas and self.intentos > 0:
            print("Palabra:", ' '.join(self.letras_adivinadas))
            print("Intentos restantes:", self.intentos)
            letra = input("Ingresa una letra: ").lower()
            self.adivinar_letra(letra)
        if '_' not in self.letras_adivinadas:
            print("¡Felicidades! ¡Has adivinado la palabra!")
        else:
            print("¡Has agotado tus intentos! La palabra era:", self.palabra_secreta)

# Uso del juego
juego = JuegoAdivinanza()
juego.jugar()
