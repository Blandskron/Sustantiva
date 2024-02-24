class ElementoQuimico:
    def __init__(self, simbolo, nombre):
        self.simbolo = simbolo
        self.nombre = nombre

    class Propiedades:
        def __init__(self, numero_atomico, masa_atomica):
            self.numero_atomico = numero_atomico
            self.masa_atomica = masa_atomica

# Ejemplo de uso
carbono = ElementoQuimico("C", "Carbono")
carbono_prop = carbono.Propiedades(6, "12.01 u")
print(f"Elemento químico: {carbono.nombre}, Símbolo: {carbono.simbolo}")
print(f"Número atómico: {carbono_prop.numero_atomico}, Masa atómica: {carbono_prop.masa_atomica}")
