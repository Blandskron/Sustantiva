class Figura:
    pass

class Rectangulo(Figura):
    pass

class Circulo(Figura):
    pass

def es_rectangulo(figura):
    return isinstance(figura, Rectangulo)

mi_rectangulo = Rectangulo()
mi_circulo = Circulo()

print(es_rectangulo(mi_rectangulo))  # True
print(es_rectangulo(mi_circulo))     # False
