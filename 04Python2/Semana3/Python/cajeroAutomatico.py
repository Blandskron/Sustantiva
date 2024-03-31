class CajeroAutomatico:
    def __init__(self):
        self.saldo = 0

    def mostrar_saldo(self):
        print(f"Tu saldo actual es: ${self.saldo}")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Has depositado: ${cantidad}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Has retirado: ${cantidad}")

def main():
    cajero = CajeroAutomatico()
    while True:
        print("\nBienvenido al Cajero Automático")
        print("1. Mostrar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            cajero.mostrar_saldo()
        elif opcion == '2':
            cantidad = float(input("Ingresa la cantidad a depositar: "))
            cajero.depositar(cantidad)
        elif opcion == '3':
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            cajero.retirar(cantidad)
        elif opcion == '4':
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
