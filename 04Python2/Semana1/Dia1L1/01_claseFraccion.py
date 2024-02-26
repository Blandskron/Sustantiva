class Fraccion:
    def __init__(self, numerador, denominador):
        """
        Constructor de la clase Fraccion.

        Args:
        - numerador (int): El numerador de la fracción.
        - denominador (int): El denominador de la fracción.
        """
        self.numerador = numerador          # Asigna el numerador proporcionado al atributo 'numerador'
        self.denominador = denominador      # Asigna el denominador proporcionado al atributo 'denominador'

    def mostrar_fraccion(self):
        """Método para mostrar la fracción en formato 'numerador/denominador'."""
        print(f"{self.numerador}/{self.denominador}")  # Imprime la fracción en formato numerador/denominador

    def sumar(self, otra_fraccion):
        """
        Método para sumar dos fracciones.

        Args:
        - otra_fraccion (Fraccion): La otra fracción que se va a sumar.

        Returns:
        - Fraccion: La fracción resultante de la suma.
        """
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)  # Devuelve una nueva instancia de Fraccion con la suma

# Crear una instancia de Fraccion
fraccion1 = Fraccion(1, 2)    # Crea una fracción 1/2
fraccion2 = Fraccion(1, 3)    # Crea una fracción 1/3
resultado = fraccion1.sumar(fraccion2)  # Suma las dos fracciones
resultado.mostrar_fraccion()   # Muestra el resultado de la suma
