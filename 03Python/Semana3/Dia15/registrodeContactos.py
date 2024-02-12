class RegistroContactos:
    def __init__(self):
        self.lista_contactos = []

    def agregar_contacto(self, nombre, telefono):
        self.lista_contactos.append((nombre, telefono))
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if self.lista_contactos:
            print("Lista de contactos:")
            for nombre, telefono in self.lista_contactos:
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("No hay contactos en el registro.")


# Crear instancia del registro de contactos
registro = RegistroContactos()

# Agregar contactos
registro.agregar_contacto("Juan", "123456789")
registro.agregar_contacto("María", "987654321")

# Mostrar contactos
registro.mostrar_contactos()
