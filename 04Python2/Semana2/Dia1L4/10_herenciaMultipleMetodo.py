class A:
    def metodo(self):
        print("Método de la clase A")


class B:
    def metodo(self):
        print("Método de la clase B")


class C(A, B):
    def metodo_c(self):
        print("Método de la clase C")


objeto_c = C()
objeto_c.metodo()   # Salida: Método de la clase A
objeto_c.metodo_c() # Salida: Método de la clase C
