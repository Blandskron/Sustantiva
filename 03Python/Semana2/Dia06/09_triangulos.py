# Solicitar al usuario que ingrese las longitudes de los lados de un triángulo
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si todos los lados son iguales, lo que indica un triángulo equilátero
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
# Verificar si al menos dos lados son iguales, lo que indica un triángulo isósceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
# Si ningún par de lados es igual, entonces es un triángulo escaleno
else:
    print("El triángulo es escaleno.")
