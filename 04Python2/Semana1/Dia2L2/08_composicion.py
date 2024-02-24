class Motor:
    def arrancar(self):
        return "Motor arrancado"

    def apagar(self):
        return "Motor apagado"

class Auto:
    def __init__(self):
        self.motor = Motor()  # Composición: Auto contiene un Motor

    def encender_auto(self):
        return self.motor.arrancar()

    def apagar_auto(self):
        return self.motor.apagar()

auto = Auto()
print(auto.encender_auto())  # Salida: Motor arrancado
print(auto.apagar_auto())  # Salida: Motor apagado
