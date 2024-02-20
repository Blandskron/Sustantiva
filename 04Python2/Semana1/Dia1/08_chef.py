class Chef:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def preparar_plato(self, plato):
        print(f"El chef {self.nombre} está preparando {plato}.")

    def mostrar_especialidad(self):
        print(f"El chef {self.nombre} es especialista en cocina {self.especialidad}.")

# Crear una instancia de Chef
chef_juan = Chef("Juan", "Francesa")
chef_juan.preparar_plato("Filet mignon")
chef_juan.mostrar_especialidad()
