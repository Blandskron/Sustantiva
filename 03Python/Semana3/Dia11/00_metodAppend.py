# Creamos una lista vacía para almacenar números
numeros = []

# Solicitamos al usuario que ingrese 5 números enteros y los agregamos a la lista utilizando append()
print("Ingrese 5 números enteros:")

# Iteramos 5 veces para recibir los números del usuario
for i in range(5):
    # Solicitamos al usuario que ingrese un número entero y lo convertimos a entero
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    # Agregamos el número a la lista utilizando el método append()
    numeros.append(numero)

# Imprimimos la lista original
print("Lista de números ingresados:", numeros)
