class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Instanciar un perro
mi_perro = Perro("Buddy", "Labrador", 3)
print("Mi perro se llama", mi_perro.nombre, "es de raza", mi_perro.raza, "y tiene", mi_perro.edad, "años")
