class Vehiculo:
    def conducir(self):
        print("Conduciendo un vehículo")


class Coche(Vehiculo):
    def conducir(self):
        print("Conduciendo un coche")


class Avion(Vehiculo):
    def conducir(self):
        print("Volando un avión")


class AvionDeCombate(Avion):
    def conducir(self):
        super().conducir()
        print("Acelerando para el combate")


mi_avion_combate = AvionDeCombate()
mi_avion_combate.conducir()
