class Vehiculo:
    def __init__(self, marca, modelo):
        # Constructor de la clase Vehiculo
        self.marca = marca  # Inicializa la marca del vehículo
        self.modelo = modelo  # Inicializa el modelo del vehículo

    def obtener_marca(self):
        # Método para obtener la marca del vehículo
        return self.marca

    def obtener_modelo(self):
        # Método para obtener el modelo del vehículo
        return self.modelo


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        # Constructor de la clase Automovil que hereda de Vehiculo
        super().__init__(marca, modelo)  # Llama al constructor de la clase base
        self.color = color  # Inicializa el color del automóvil

    def obtener_color(self):
        # Método para obtener el color del automóvil
        return self.color


class Camioneta(Automovil):
    def __init__(self, marca, modelo, color, carga):
        # Constructor de la clase Camioneta que hereda de Automovil
        super().__init__(marca, modelo, color)  # Llama al constructor de la clase base
        self.carga = carga  # Inicializa la capacidad de carga de la camioneta

    def obtener_carga(self):
        # Método para obtener la capacidad de carga de la camioneta
        return self.carga


# Creación de instancias de las clases
automovil1 = Automovil("Toyota", "Corolla", "Rojo")
camioneta1 = Camioneta("Ford", "Ranger", "Negro", "500 kg")

# Acceso a los métodos y atributos de las clases
print("Marca del automóvil:", automovil1.obtener_marca())
print("Modelo del automóvil:", automovil1.obtener_modelo())
print("Color del automóvil:", automovil1.obtener_color())

print("Marca de la camioneta:", camioneta1.obtener_marca())
print("Modelo de la camioneta:", camioneta1.obtener_modelo())
print("Color de la camioneta:", camioneta1.obtener_color())
print("Carga de la camioneta:", camioneta1.obtener_carga())
