# Estructura de control if-elif-else
num = 42

if num > 50:
    print("El número es mayor que 50")
elif num < 50:
    print("El número es menor que 50")
else:
    print("El número es igual a 50")

# Estructura de control for
for i in range(5):
    print(i)

# Estructura de control while
count = 0
while count < 5:
    print(count)
    count += 1

# Sentencias break y continue en un bucle
for i in range(10):
    if i == 3:
        break  # Termina el bucle cuando i es 3
    elif i == 1:
        continue  # Salta la iteración cuando i es 1
    print(i)
