class Perros(object):
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        print("Modificando nombre..")
        self.__nombre = nuevo
        print("El nombre se ha modificado por")
        print(self.__nombre)

Rocky = Perros('Rocky')
print(Rocky.nombre)

Rocky.nombre = 'Rockycito'