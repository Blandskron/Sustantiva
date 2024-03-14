class Abuelo:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Padre(Abuelo):
    def __init__(self, nombre, abuelo):
        super().__init__(abuelo.nombre, abuelo.apellido)
        self.nombre = nombre

class Hijo(Padre):
    def __init__(self, nombre, padre):
        super().__init__(nombre, padre)

nombre_abuelo = input("Ingrese el nombre del abuelo: ")
apellido_abuelo = input("Ingrese el apellido del abuelo: ")
abuelo = Abuelo(nombre_abuelo, apellido_abuelo)

nombre_padre = input("Ingrese el nombre del padre: ")
padre = Padre(nombre_padre, abuelo)

nombre_hijo = input("Ingrese el nombre del hijo: ")
hijo = Hijo(nombre_hijo, padre)

print(f"Abuelo: {abuelo.nombre} {abuelo.apellido}")
print(f"Padre: {padre.nombre} {padre.apellido}")
print(f"Hijo: {hijo.nombre} {hijo.apellido}")
