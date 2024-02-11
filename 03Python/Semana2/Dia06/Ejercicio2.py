# Inicialización de la agenda como un diccionario vacío
agenda = {}

# Variable para controlar si el usuario desea salir del programa
salir = False

# Mensaje de bienvenida
print("**** Bienvenido a AGENDA ****\n")

# Bucle principal que permite al usuario agregar contactos a la agenda
while (not salir):
    # Solicita al usuario que ingrese un nombre y un teléfono
    nombre = input("Ingrese un nombre:\n")
    telefono = int(input("Ingrese un telefono:\n"))

    # Verifica si el nombre ya existe en la agenda
    if nombre not in agenda:
        # Si el nombre no está en la agenda, lo agrega junto con su teléfono
        agenda[nombre] = telefono
        print('Contacto guardado exitosamente!!')
    else:
        # Si el nombre ya está en la agenda, muestra un mensaje indicando que ya existe
        print('El nombre ya se encuentra en la agenda!!')

    # Pregunta al usuario si desea salir del programa
    respuesta = input("Salir? (S/N) ")

    # Si la respuesta es 'S' o 's', establece salir como True para finalizar el bucle
    if respuesta.lower() == "s":
        salir = True

# Imprime la lista de contactos almacenada en la agenda
print("Mis contactos:\n", agenda)
