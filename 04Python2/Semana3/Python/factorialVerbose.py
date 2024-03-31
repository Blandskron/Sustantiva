def factorial_verbose(n):
    if n == 0 or n == 1:
        print(f"factorial({n}) = 1")
        return 1
    else:
        print(f"factorial({n}) = {n} * factorial({n-1})")
        return n * factorial_verbose(n-1)

def hanoi_verbose(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Mover disco 1 de la varilla {from_rod} a la varilla {to_rod}")
        return
    hanoi_verbose(n-1, from_rod, aux_rod, to_rod)
    print(f"Mover disco {n} de la varilla {from_rod} a la varilla {to_rod}")
    hanoi_verbose(n-1, aux_rod, to_rod, from_rod)

# Ejemplo de uso para factorial
print("Cálculo del factorial:")
n = 5
result = factorial_verbose(n)
print(f"El resultado de factorial({n}) es {result}")

# Ejemplo de uso para Torre de Hanoi
print("\nSolución para la Torre de Hanoi:")
n = 3
hanoi_verbose(n, 'A', 'C', 'B')

