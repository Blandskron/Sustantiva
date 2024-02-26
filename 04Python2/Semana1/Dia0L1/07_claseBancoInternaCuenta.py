class Banco:
    def __init__(self, nombre):
        """
        Constructor de la clase Banco.

        Args:
        - nombre (str): El nombre del banco.
        """
        self.nombre = nombre    # Asigna el nombre del banco al atributo 'nombre'
        self.cuentas = []       # Inicializa una lista vacía para almacenar las cuentas del banco

    def agregar_cuenta(self, numero, saldo):
        """
        Método para agregar una nueva cuenta al banco.

        Args:
        - numero (str): El número de la cuenta.
        - saldo (float): El saldo inicial de la cuenta.
        """
        nueva_cuenta = self.Cuenta(numero, saldo)  # Crea una nueva instancia de la clase Cuenta
        self.cuentas.append(nueva_cuenta)          # Agrega la nueva cuenta a la lista de cuentas del banco

    class Cuenta:
        def __init__(self, numero, saldo):
            """
            Constructor de la clase Cuenta.

            Args:
            - numero (str): El número de la cuenta.
            - saldo (float): El saldo inicial de la cuenta.
            """
            self.numero = numero    # Asigna el número de la cuenta al atributo 'numero'
            self.saldo = saldo      # Asigna el saldo inicial de la cuenta al atributo 'saldo'

        def mostrar_info(self):
            """Método para mostrar la información de la cuenta."""
            print(f"Número de cuenta: {self.numero}, Saldo: ${self.saldo}")


# Crear instancia de la clase Banco y agregar cuentas
banco = Banco("Banco XYZ")     # Crea una instancia de Banco con nombre "Banco XYZ"
banco.agregar_cuenta("123456", 5000)  # Agrega una cuenta al banco con número "123456" y saldo inicial $5000
banco.agregar_cuenta("789012", 10000) # Agrega otra cuenta al banco con número "789012" y saldo inicial $10000

# Mostrar información de las cuentas del banco
for cuenta in banco.cuentas:   # Itera sobre las cuentas del banco
    cuenta.mostrar_info()       # Muestra la información de cada cuenta
