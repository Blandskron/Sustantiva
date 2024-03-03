class Automovil:
    def __init__(self, marca, modelo, color, num_puertas, placa):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.num_puertas = num_puertas
        self.placa = placa

    def consultar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Número de puertas: {self.num_puertas}")
        print(f"Placa: {self.placa}")
        print()

# Crear 5 instancias de la clase Automovil con la información ingresada por el usuario
autos = []
for i in range(5):
    print(f"Ingrese la información del vehículo {i + 1}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    color = input("Color: ")
    num_puertas = input("Número de puertas: ")
    placa = input("Placa: ")

    auto = Automovil(marca, modelo, color, num_puertas, placa)
    autos.append(auto)

# Consultar la información de cada vehículo
print("\nInformación de los vehículos:")
for idx, auto in enumerate(autos, start=1):
    print(f"Vehículo {idx}:")
    auto.consultar_informacion()
