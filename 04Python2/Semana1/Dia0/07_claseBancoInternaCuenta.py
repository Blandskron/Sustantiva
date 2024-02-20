class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, numero, saldo):
        nueva_cuenta = self.Cuenta(numero, saldo)
        self.cuentas.append(nueva_cuenta)

    class Cuenta:
        def __init__(self, numero, saldo):
            self.numero = numero
            self.saldo = saldo

        def mostrar_info(self):
            print(f"Número de cuenta: {self.numero}, Saldo: ${self.saldo}")


# Crear instancia de la clase Banco y agregar cuentas
banco = Banco("Banco XYZ")
banco.agregar_cuenta("123456", 5000)
banco.agregar_cuenta("789012", 10000)

# Mostrar información de las cuentas del banco
for cuenta in banco.cuentas:
    cuenta.mostrar_info()
