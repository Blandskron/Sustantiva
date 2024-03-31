class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def descripcion(self):
        return f"{super().descripcion()} de color {self.color}"


mi_coche = Coche("Toyota", "Corolla", "rojo")
print(mi_coche.descripcion())  # Salida: Vehículo: Toyota Corolla de color rojo
