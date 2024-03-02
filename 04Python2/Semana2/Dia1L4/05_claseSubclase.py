class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print("¡Guau! ¡Guau!")


mi_perro = Perro("Bobby", "Labrador")
mi_perro.comer()  # Salida: Bobby está comiendo.
mi_perro.ladrar()  # Salida: ¡Guau! ¡Guau!
