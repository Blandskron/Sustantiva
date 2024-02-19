numero1 = True
numero2 = True
numero3 = True

while True:

    while (numero1):
        try:
            num1 = int(input("Ingrese el primer numero (1 de 3):\n"))
            numero1 = False
        except ValueError:
            print("Ingrese un numero Valido")

    while (numero2):
        try:
            num2 = int(input("Ingrese el primer numero (2 de 3):\n"))
            numero2 = False
        except ValueError:
            print("Ingrese un numero Valido")

    while (numero3):
        try:
            num3 = int(input("Ingrese el primer numero (3 de 3):\n"))
            numero3 = False
        except ValueError:
            print("Ingrese un numero Valido")

    if num1 > num2 and num1 > num3:
        print("\nEl numero mayor de los tres es:", num1)
        break
    elif num2 > num1 and num2 > num3:
        print("\nEl numero mayor de los tres es:", num2)
        break
    else:
        print("\nEl numero mayor de los tres es:", num3)
        break
