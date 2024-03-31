class Volador:
    def volar(self):
        print("Volando...")


class Nadador:
    def nadar(self):
        print("Nadando...")


class Pato(Volador, Nadador):
    pass


pato = Pato()
pato.volar()  # Salida: Volando...
pato.nadar()  # Salida: Nadando...
