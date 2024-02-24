class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Instanciar un automóvil
mi_auto = Automovil("Toyota", "Corolla", "Negro")
print("Mi auto es un", mi_auto.marca, mi_auto.modelo, "de color", mi_auto.color)
