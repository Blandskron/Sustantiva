class Car:
    # Constructor que inicializa los atributos de la clase
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.state = False  # Inicialmente el auto está apagado
    
    # Método para encender el automóvil
    def turnOn(self):
        self.state = True
    
    # Método para apagar el automóvil
    def turnOff(self):
        self.state = False
    
    # Método para conducir el automóvil una cierta distancia en kilómetros
    def drive(self, kilometers):
        # Verifica si el automóvil está encendido
        if self.state:
            self.mileage += kilometers  # Incrementa el kilometraje del automóvil
        else:
            # Si el automóvil está apagado, lanza una excepción
            raise Exception("El auto está apagado")

# Creación de una instancia de la clase Car
response = Car("Toyota", "Corolla", 2020, 0)

# Accediendo al atributo 'brand' de la instancia 'response' de la clase 'Car'
print(response.brand)
