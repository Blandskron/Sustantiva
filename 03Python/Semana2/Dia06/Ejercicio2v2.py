agenda = {}

def nombreValido(nombreValido):
    
    return nombreValido.isalpha()

salir = False
nombreCorrecto = False
numeroCorrecto = False

print("**** Bienvenido a AGENDA ****\n")

while (not salir):
    while (not nombreCorrecto):
        nombre = input("Ingrese un nombre:\n")
        validarNombre = nombreValido(nombre)
        if validarNombre == True:
            print("Nombre Valido")
            nombreCorrecto = True
        else:
            print("Ingrese un nombre sin numeros")

    while (not numeroCorrecto):
        try:
            telefono = int(input("Ingrese un telefono:\n"))
            numeroCorrecto = True
        except ValueError:
            print("Ingrese Solo numeros")

    if nombre not in agenda:
        agenda[nombre] = telefono
        nombreCorrecto = False
        numeroCorrecto = False
        print('Contacto guardado exitosamente!!')
    else:
        print('El nombre ya se encuentra en la agenda!!')

    respuesta = input("Salir? (S/N) ")

    if respuesta.lower() == "s":
        salir = True

print("Mis contactos:\n", agenda)
