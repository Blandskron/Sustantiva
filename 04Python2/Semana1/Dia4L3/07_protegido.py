class EjemploProtegido:
    def __init__(self):
        self._protegido = "Este es un atributo protegido"

# Creación de instancia de la clase
objeto_protegido = EjemploProtegido()

# Acceso al atributo protegido
print(objeto_protegido._protegido)
