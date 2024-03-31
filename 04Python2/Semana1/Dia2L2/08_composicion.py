class Motor:
    def arrancar(self):
        """Método para arrancar el motor."""
        return "Motor arrancado"

    def apagar(self):
        """Método para apagar el motor."""
        return "Motor apagado"

class Auto:
    def __init__(self):
        """Constructor de la clase Auto."""
        self.motor = Motor()  # Instancia de la clase Motor dentro de la clase Auto

    def encender_auto(self):
        """Método para encender el auto."""
        return self.motor.arrancar()  # Llama al método arrancar del motor

    def apagar_auto(self):
        """Método para apagar el auto."""
        return self.motor.apagar()  # Llama al método apagar del motor

# Crear una instancia de la clase Auto
auto = Auto()

# Llamar al método encender_auto() de la instancia de Auto
print(auto.encender_auto())  # Salida: Motor arrancado

# Llamar al método apagar_auto() de la instancia de Auto
print(auto.apagar_auto())    # Salida: Motor apagado
