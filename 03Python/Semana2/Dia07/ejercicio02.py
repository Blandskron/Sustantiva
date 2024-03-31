# Bucle externo que recorre los números del 1 al 10
for a in range(1, 11):
    
    # Bucle interno que recorre los números del 1 al 10 para multiplicar con 'a'
    for b in range(1, 11):
        # Imprime la multiplicación de 'a' y 'b' junto con un mensaje
        print(a, "*", b, "=", a*b)
