class Coche:
    def __init__(self, marca, modelo, año):
        """
        Constructor de la clase Coche.

        Args:
        - marca (str): La marca del coche.
        - modelo (str): El modelo del coche.
        - año (int): El año de fabricación del coche.
        """
        self.marca = marca      # Asigna la marca del coche al atributo 'marca'
        self.modelo = modelo    # Asigna el modelo del coche al atributo 'modelo'
        self.año = año          # Asigna el año de fabricación del coche al atributo 'año'
        self.encendido = False  # Inicializa el estado del coche como apagado al momento de la creación

    def encender(self):
        """Método para encender el coche."""
        self.encendido = True   # Cambia el estado del coche a encendido

    def apagar(self):
        """Método para apagar el coche."""
        self.encendido = False  # Cambia el estado del coche a apagado

    def estado(self):
        """
        Método para obtener el estado del coche.

        Returns:
        - str: "Encendido" si el coche está encendido, "Apagado" si está apagado.
        """
        return "Encendido" if self.encendido else "Apagado"  # Devuelve el estado del coche como cadena


# Crear instancia de la clase Coche
coche = Coche("Toyota", "Corolla", 2020)  # Crea una instancia de Coche con la marca Toyota, modelo Corolla y año 2020

# Encender y apagar el coche
coche.encender()                           # Enciende el coche
print(f"Estado del coche: {coche.estado()}")  # Imprime: Encendido
coche.apagar()                             # Apaga el coche
print(f"Estado del coche: {coche.estado()}")  # Imprime: Apagado
