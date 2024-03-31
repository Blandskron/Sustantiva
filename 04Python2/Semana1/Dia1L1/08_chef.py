class Chef:
    def __init__(self, nombre, especialidad):
        """
        Constructor de la clase Chef.

        Args:
        - nombre (str): El nombre del chef.
        - especialidad (str): La especialidad culinaria del chef.
        """
        self.nombre = nombre                # Asigna el nombre del chef al atributo 'nombre'
        self.especialidad = especialidad    # Asigna la especialidad del chef al atributo 'especialidad'

    def preparar_plato(self, plato):
        """
        Método para indicar que el chef está preparando un plato específico.

        Args:
        - plato (str): El nombre del plato que el chef está preparando.
        """
        print(f"El chef {self.nombre} está preparando {plato}.")

    def mostrar_especialidad(self):
        """Método para mostrar la especialidad del chef."""
        print(f"El chef {self.nombre} es especialista en cocina {self.especialidad}.")

# Crear una instancia de Chef
chef_juan = Chef("Juan", "Francesa")   # Crea una instancia de Chef con nombre "Juan" y especialidad "Francesa"

# Llamar a los métodos de la instancia de Chef
chef_juan.preparar_plato("Filet mignon")  # Llama al método preparar_plato para indicar que el chef Juan está preparando Filet mignon
chef_juan.mostrar_especialidad()          # Llama al método mostrar_especialidad para mostrar que el chef Juan es especialista en cocina Francesa
