class Empresa:
    def __init__(self, nombre):
        """
        Constructor de la clase Empresa.

        Args:
        - nombre (str): El nombre de la empresa.
        """
        self.nombre = nombre    # Asigna el nombre de la empresa al atributo 'nombre'
        self.empleados = []     # Inicializa una lista vacía para almacenar los empleados de la empresa

    def contratar_empleado(self, nombre, salario):
        """
        Método para contratar un nuevo empleado.

        Args:
        - nombre (str): El nombre del empleado.
        - salario (float): El salario del empleado.
        """
        nuevo_empleado = self.Empleado(nombre, salario)  # Crea una nueva instancia de la clase Empleado
        self.empleados.append(nuevo_empleado)           # Agrega el nuevo empleado a la lista de empleados de la empresa

    class Empleado:
        def __init__(self, nombre, salario):
            """
            Constructor de la clase Empleado.

            Args:
            - nombre (str): El nombre del empleado.
            - salario (float): El salario del empleado.
            """
            self.nombre = nombre    # Asigna el nombre del empleado al atributo 'nombre'
            self.salario = salario  # Asigna el salario del empleado al atributo 'salario'

        def mostrar_info(self):
            """Método para mostrar la información del empleado."""
            print(f"Nombre: {self.nombre}, Salario: ${self.salario}")


# Crear instancia de la clase Empresa y contratar empleados
empresa = Empresa("Empresa ABC")       # Crea una instancia de Empresa con nombre "Empresa ABC"
empresa.contratar_empleado("María", 3000)   # Contrata a un empleado llamado "María" con un salario de $3000
empresa.contratar_empleado("Pedro", 3500)   # Contrata a otro empleado llamado "Pedro" con un salario de $3500

# Mostrar información de los empleados de la empresa
for empleado in empresa.empleados:    # Itera sobre la lista de empleados de la empresa
    empleado.mostrar_info()            # Muestra la información de cada empleado
