# Pedir al usuario que ingrese un número del 1 al 100
numero = int(input("Ingrese un número del 1 al 100: "))

# Imprimir los números pares o impares según corresponda
if numero % 2 == 0:
    print(f"Números pares desde {numero} hasta 100:")
    for i in range(numero, 101, 2):
        print(i, end=" ")
    print()  # Imprimir un salto de línea al final
else:
    print(f"Números impares desde {numero} hasta 99:")
    for i in range(numero, 100, 2):
        print(i, end=" ")
    print()  # Imprimir un salto de línea al final
