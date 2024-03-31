class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")


class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


perro = Perro("Bobby")
gato = Gato("Minino")

print(perro.hablar())  # Salida: Bobby dice: ¡Guau!
print(gato.hablar())   # Salida: Minino dice: ¡Miau!
