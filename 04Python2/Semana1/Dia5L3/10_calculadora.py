class CalculadoraInteractiva:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        else:
            return a / b

    def ejecutar(self):
        print("¡Bienvenido a la calculadora interactiva!")
        while True:
            print("Opciones:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '5':
                print("¡Hasta luego!")
                break
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if opcion == '1':
                print("El resultado de la suma es:", self.sumar(num1, num2))
            elif opcion == '2':
                print("El resultado de la resta es:", self.restar(num1, num2))
            elif opcion == '3':
                print("El resultado de la multiplicación es:", self.multiplicar(num1, num2))
            elif opcion == '4':
                print("El resultado de la división es:", self.dividir(num1, num2))
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

# Uso de la calculadora interactiva
calculadora = CalculadoraInteractiva()
calculadora.ejecutar()
