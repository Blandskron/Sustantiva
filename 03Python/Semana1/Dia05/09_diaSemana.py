# Determinar el día de la semana según el número ingresado
dia_numero = int(input("Ingrese un número del 1 al 7: "))

if dia_numero == 1:
    print("Lunes")
elif dia_numero == 2:
    print("Martes")
elif dia_numero == 3:
    print("Miércoles")
elif dia_numero == 4:
    print("Jueves")
elif dia_numero == 5:
    print("Viernes")
elif dia_numero == 6:
    print("Sábado")
elif dia_numero == 7:
    print("Domingo")
else:
    print("Número inválido. Debe ser del 1 al 7.")
