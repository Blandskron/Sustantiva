class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def iniciar(self):
        print(f"El motor de tipo {self.tipo} ha sido iniciado")


class Puerta:
    def __init__(self, color):
        self.color = color

    def abrir(self):
        print(f"La puerta de color {self.color} ha sido abierta")

    def cerrar(self):
        print(f"La puerta de color {self.color} ha sido cerrada")


class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("gasolina")
        self.puertas = [Puerta("rojo"), Puerta("rojo"), Puerta("rojo"), Puerta("rojo")]

    def encender(self):
        self.motor.iniciar()
        print(f"El automóvil {self.marca} {self.modelo} ha sido encendido")

    def abrir_puertas(self):
        for puerta in self.puertas:
            puerta.abrir()

    def cerrar_puertas(self):
        for puerta in self.puertas:
            puerta.cerrar()


# Creación de instancia de Automovil
mi_auto = Automovil("Toyota", "Corolla")

# Acciones con el automóvil
mi_auto.encender()
mi_auto.abrir_puertas()
mi_auto.cerrar_puertas()
