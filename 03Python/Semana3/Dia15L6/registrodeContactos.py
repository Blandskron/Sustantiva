class RegistroContactos:
    def __init__(self):
        self.lista_contactos = []  # Inicializa una lista vacía para almacenar contactos

    def agregar_contacto(self, nombre, telefono):
        self.lista_contactos.append((nombre, telefono))  # Agrega un nuevo contacto como una tupla (nombre, teléfono)
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if self.lista_contactos:  # Verifica si hay contactos en la lista
            print("Lista de contactos:")
            for nombre, telefono in self.lista_contactos:  # Muestra los contactos
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("No hay contactos en el registro.")  # Muestra un mensaje si no hay contactos en la lista


# Crear instancia del registro de contactos
registro = RegistroContactos()

# Agregar contactos
registro.agregar_contacto("Juan", "123456789")
registro.agregar_contacto("María", "987654321")

# Mostrar contactos
registro.mostrar_contactos()
