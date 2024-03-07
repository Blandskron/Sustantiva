class Perros(object):
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        """Getter para obtener el nombre del perro."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo):
        """Setter para modificar el nombre del perro."""
        print("Modificando nombre..")
        self.__nombre = nuevo
        print("El nombre se ha modificado por")
        print(self.__nombre)

# Crear una instancia de la clase Perros con el nombre 'Rocky'
Rocky = Perros('Rocky')

# Acceder al nombre del perro utilizando el getter
print(Rocky.nombre)  # Salida: Rocky

# Modificar el nombre del perro utilizando el setter
Rocky.nombre = 'Rockycito'
