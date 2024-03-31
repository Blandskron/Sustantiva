class A:
    pass

class B(A):
    pass

class C(B):
    pass

objeto_c = C()

print(isinstance(objeto_c, A))  # True
print(isinstance(objeto_c, B))  # True
print(isinstance(objeto_c, C))  # True
