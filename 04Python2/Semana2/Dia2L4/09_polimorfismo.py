class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

def hacer_hablar(animal):
    print(animal.hablar())

# Ejemplo de polimorfismo
perro = Perro()
gato = Gato()

hacer_hablar(perro)  # Imprime: Guau!
hacer_hablar(gato)   # Imprime: Miau!
