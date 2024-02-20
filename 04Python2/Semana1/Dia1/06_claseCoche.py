class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def estado(self):
        return "Encendido" if self.encendido else "Apagado"


# Crear instancia de la clase Coche
coche = Coche("Toyota", "Corolla", 2020)

# Encender y apagar el coche
coche.encender()
print(f"Estado del coche: {coche.estado()}")  # Imprime: Encendido
coche.apagar()
print(f"Estado del coche: {coche.estado()}")  # Imprime: Apagado
