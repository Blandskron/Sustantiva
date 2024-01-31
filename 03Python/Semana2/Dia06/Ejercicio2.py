agenda = {}

salir = False
print("**** Bienvenido a AGENDA **** \n")

while (not salir):

    nombre = input("Ingrese un nombre: \n")
    telefono = int(input("Ingrese un telefono: \n"))

    if ( nombre not in agenda):

        agenda[nombre] = telefono
        print('Contacto guardado exitosamente!!')
    else:
        print('El nombre ya se encuentra en la agenda!!')

    respuesta = input("Salir? (S/N) ")

    if (respuesta == "S") or (respuesta == "s"):
        salir = True

print("Mis contactos: \n", agenda)
