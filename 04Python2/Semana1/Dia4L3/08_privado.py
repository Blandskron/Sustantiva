class EjemploPrivado:
    def __init__(self):
        self.__privado = "Este es un atributo privado"

    def obtener_privado(self):
        return self.__privado

# Creación de instancia de la clase
objeto_privado = EjemploPrivado()

# Intento de acceso al atributo privado
# Esto generará un error ya que no se puede acceder directamente a un atributo privado desde fuera de la clase
# print(objeto_privado.__privado)

# Acceso al atributo privado a través de un método de la clase
print(objeto_privado.obtener_privado())
