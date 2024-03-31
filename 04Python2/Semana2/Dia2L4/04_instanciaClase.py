class Animal:
    pass

class Perro(Animal):
    pass

mi_animal = Animal()
mi_perro = Perro()

print(isinstance(mi_animal, Animal))  # True
print(isinstance(mi_animal, Perro))    # False

print(isinstance(mi_perro, Animal))    # True
print(isinstance(mi_perro, Perro))      # True
