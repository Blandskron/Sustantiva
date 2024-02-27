# Definición de la clase EjemploProtegido
class EjemploProtegido:
    # Método constructor
    def __init__(self):
        # Inicialización del atributo protegido
        self._protegido = "Este es un atributo protegido"

# Creación de una instancia de la clase EjemploProtegido
objeto_protegido = EjemploProtegido()

# Acceso al atributo protegido e impresión de su valor
print(objeto_protegido._protegido)
