class ElementoQuimico:
    def __init__(self, simbolo, nombre):
        """
        Constructor de la clase ElementoQuimico.

        Args:
        - simbolo (str): El símbolo del elemento químico.
        - nombre (str): El nombre del elemento químico.
        """
        self.simbolo = simbolo
        self.nombre = nombre

    class Propiedades:
        def __init__(self, numero_atomico, masa_atomica):
            """
            Constructor de la clase Propiedades.

            Args:
            - numero_atomico (int): El número atómico del elemento químico.
            - masa_atomica (str): La masa atómica del elemento químico.
            """
            self.numero_atomico = numero_atomico
            self.masa_atomica = masa_atomica

# Ejemplo de uso
carbono = ElementoQuimico("C", "Carbono")
carbono_prop = carbono.Propiedades(6, "12.01 u")
print(f"Elemento químico: {carbono.nombre}, Símbolo: {carbono.simbolo}")
print(f"Número atómico: {carbono_prop.numero_atomico}, Masa atómica: {carbono_prop.masa_atomica}")
