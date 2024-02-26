class MiClase:
    def __init__(self, x):
        self.__privado = x  # Atributo privado
        self._protegido = 2 * x  # Atributo protegido
        self.publico = 3 * x  # Atributo público

    def obtener_privado(self):
        # Método para obtener el atributo privado
        return self.__privado

    def __metodo_privado(self):
        # Método privado
        print("Este es un método privado")

    def _metodo_protegido(self):
        # Método protegido
        print("Este es un método protegido")

    def metodo_publico(self):
        # Método público que llama a los métodos privado y protegido
        print("Este es un método público")
        self.__metodo_privado()
        self._metodo_protegido()


# Creación de instancia de la clase MiClase
objeto = MiClase(5)

# Acceso a los atributos y métodos
print("Atributo público:", objeto.publico)
print("Atributo protegido:", objeto._protegido)
print("Atributo privado:", objeto.obtener_privado())

objeto.metodo_publico()
