# Definición de la clase CuentaBancaria
class CuentaBancaria:
    # Método constructor que inicializa los atributos de la cuenta: número de cuenta, titular y saldo
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta  # Asigna el número de cuenta proporcionado al atributo numero_cuenta
        self.titular = titular              # Asigna el titular proporcionado al atributo titular
        self.saldo = saldo                  # Asigna el saldo proporcionado al atributo saldo

    # Método para depositar dinero en la cuenta
    def depositar(self, cantidad):
        self.saldo += cantidad  # Incrementa el saldo de la cuenta con la cantidad depositada
        # Muestra un mensaje indicando la cantidad depositada y el saldo actual de la cuenta
        print(f"Se depositaron {cantidad} euros en la cuenta. Saldo actual: {self.saldo} euros")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        # Verifica si hay suficiente saldo en la cuenta para realizar la operación de retiro
        if cantidad <= self.saldo:
            self.saldo -= cantidad  # Reduce el saldo de la cuenta en la cantidad retirada
            # Muestra un mensaje indicando la cantidad retirada y el saldo actual de la cuenta
            print(f"Se retiraron {cantidad} euros de la cuenta. Saldo actual: {self.saldo} euros.")
        else:
            print("No hay suficiente saldo en la cuenta.")  # Muestra un mensaje si no hay suficiente saldo

    # Método para mostrar el saldo actual de la cuenta
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo} euros.")  # Muestra el saldo actual de la cuenta


# Creación de dos instancias de la clase CuentaBancaria con diferentes parámetros
cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000)
cuenta2 = CuentaBancaria("987654321", "María López", 500)

# Operaciones con las cuentas utilizando los métodos de la clase
cuenta1.depositar(500)
cuenta2.retirar(200)

# Mostrar el saldo de ambas cuentas
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()
