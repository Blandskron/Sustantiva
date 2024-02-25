class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        """
        Constructor de la clase CuentaBancaria.

        Args:
        - titular (str): El titular de la cuenta.
        - saldo_inicial (float): El saldo inicial de la cuenta.
        """
        self.titular = titular            # Asigna el titular de la cuenta al atributo 'titular'
        self.saldo = saldo_inicial        # Asigna el saldo inicial al atributo 'saldo'

    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.

        Args:
        - cantidad (float): La cantidad a depositar.
        """
        self.saldo += cantidad            # Incrementa el saldo de la cuenta con la cantidad depositada

    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.

        Args:
        - cantidad (float): La cantidad a retirar.
        """
        if cantidad <= self.saldo:        # Verifica si hay suficiente saldo para realizar la operación
            self.saldo -= cantidad        # Reduce el saldo de la cuenta
        else:
            print("Saldo insuficiente.")  # Si no hay suficiente saldo, muestra un mensaje de saldo insuficiente


# Crear instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)  # Crea una instancia de CuentaBancaria con titular Juan Pérez y saldo inicial de 1000

# Realizar transacciones
cuenta.depositar(500)          # Deposita 500 en la cuenta
cuenta.retirar(200)            # Retira 200 de la cuenta

# Imprimir el saldo actual
print(f"Saldo actual de {cuenta.titular}: {cuenta.saldo}")  # Imprime el saldo actual del titular de la cuenta
