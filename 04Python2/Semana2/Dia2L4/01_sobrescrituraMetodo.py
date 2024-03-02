class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de un animal")


class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau! ¡Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau! ¡Miau!")


mi_perro = Perro()
mi_perro.hacer_sonido()  # Salida: ¡Guau! ¡Guau!

mi_gato = Gato()
mi_gato.hacer_sonido()   # Salida: ¡Miau! ¡Miau!
