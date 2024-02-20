class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_fraccion(self):
        print(f"{self.numerador}/{self.denominador}")

    def sumar(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

# Crear una instancia de Fraccion
fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(1, 3)
resultado = fraccion1.sumar(fraccion2)
resultado.mostrar_fraccion()
