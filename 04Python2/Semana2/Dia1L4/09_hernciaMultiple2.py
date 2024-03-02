class Persona:
    def saludar(self):
        print("Hola, soy una persona.")


class Superheroe:
    def saludar(self):
        print("Hola, soy un superhéroe.")


class SuperheroeVolador(Persona, Superheroe):
    pass


superman = SuperheroeVolador()
superman.saludar()  # Salida: Hola, soy una persona.
