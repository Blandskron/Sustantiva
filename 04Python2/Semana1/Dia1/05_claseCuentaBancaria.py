class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente.")


# Crear instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)

# Realizar transacciones
cuenta.depositar(500)
cuenta.retirar(200)
print(f"Saldo actual de {cuenta.titular}: {cuenta.saldo}")  # Imprime el saldo actual
