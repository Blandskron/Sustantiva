# Verificar si una persona puede ver una película según su edad
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Puede ver la película para adultos.")
elif edad >= 13:
    print("Puede ver la película para adolescentes.")
else:
    print("Debe ser mayor de 13 años para ver esta película.")
