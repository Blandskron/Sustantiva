class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        self.imprimir_estado()

    def frenar(self):
        if self.velocidad >= 5:
            self.velocidad -= 5
        else:
            self.velocidad = 0
        self.imprimir_estado()

    def imprimir_estado(self):
        print(f"Estado del vehículo:\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nVelocidad: {self.velocidad} km/h\n")

def main():
    # Crear un vehículo
    vehiculo = Vehiculo("Toyota", "Corolla", "Rojo", 0)

    # Acelerar y frenar el vehículo
    vehiculo.acelerar()
    vehiculo.frenar()
    vehiculo.frenar()  # Frenar cuando la velocidad es 0

if __name__ == "__main__":
    main()
