class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} euros en la cuenta. Saldo actual: {self.saldo} euros.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} euros de la cuenta. Saldo actual: {self.saldo} euros.")
        else:
            print("No hay suficiente saldo en la cuenta.")

    def mostrar_saldo(self):
        print(f"El saldo de la cuenta es: {self.saldo} euros.")


# Creación de dos instancias de la clase CuentaBancaria
cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000)
cuenta2 = CuentaBancaria("987654321", "María López", 500)

# Operaciones con las cuentas utilizando los métodos de la clase
cuenta1.depositar(500)
cuenta2.retirar(200)

# Mostrar el saldo de ambas cuentas
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()
