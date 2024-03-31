def suma_si_entero(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Ambos argumentos deben ser enteros"

print(suma_si_entero(3, 5))    # 8
print(suma_si_entero(3.5, 5))  # Ambos argumentos deben ser enteros
