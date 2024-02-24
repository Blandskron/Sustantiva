class RedSocial:
    def __init__(self, nombre, usuarios=[]):
        self.nombre = nombre
        self.usuarios = usuarios

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"¡Bienvenido {usuario} a {self.nombre}!")

    def mostrar_usuarios(self):
        print(f"Usuarios de {self.nombre}:")
        for usuario in self.usuarios:
            print("-", usuario)

# Crear una instancia de RedSocial
facebook = RedSocial("Facebook")
facebook.agregar_usuario("Juan")
facebook.agregar_usuario("María")
facebook.mostrar_usuarios()
