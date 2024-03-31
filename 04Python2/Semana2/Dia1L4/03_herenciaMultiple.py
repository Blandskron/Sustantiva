class A:
    def metodo(self):
        print("Método de la clase A")


class B(A):
    def metodo(self):
        print("Método de la clase B")


class C(A):
    def metodo(self):
        print("Método de la clase C")


class D(B, C):
    pass


objeto_d = D()
objeto_d.metodo()  # Salida: Método de la clase B
