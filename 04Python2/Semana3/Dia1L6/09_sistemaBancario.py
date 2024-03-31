class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a retirar es inválida o excede el saldo disponible.")


def main():
    # Crear cuentas bancarias
    cuenta1 = CuentaBancaria("Juan Pérez", 500)
    cuenta2 = CuentaBancaria("María López", 1000)

    # Realizar transacciones
    cuenta1.depositar(300)
    cuenta1.retirar(200)

    cuenta2.depositar(500)
    cuenta2.retirar(1500)


if __name__ == "__main__":
    main()
