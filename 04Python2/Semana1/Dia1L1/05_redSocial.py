class RedSocial:
    def __init__(self, nombre, usuarios=[]):
        """
        Constructor de la clase RedSocial.

        Args:
        - nombre (str): El nombre de la red social.
        - usuarios (list): Una lista opcional de usuarios (por defecto, una lista vacía).
        """
        self.nombre = nombre    # Asigna el nombre de la red social al atributo 'nombre'
        self.usuarios = usuarios  # Asigna la lista de usuarios proporcionada al atributo 'usuarios' (o crea una lista vacía si no se proporciona)

    def agregar_usuario(self, usuario):
        """
        Método para agregar un usuario a la red social.

        Args:
        - usuario (str): El nombre del usuario a agregar.
        """
        self.usuarios.append(usuario)  # Agrega el usuario a la lista de usuarios de la red social
        print(f"¡Bienvenido {usuario} a {self.nombre}!")  # Imprime un mensaje de bienvenida al usuario

    def mostrar_usuarios(self):
        """Método para mostrar los usuarios de la red social."""
        print(f"Usuarios de {self.nombre}:")
        for usuario in self.usuarios:
            print("-", usuario)  # Imprime cada usuario de la lista de usuarios

# Crear una instancia de RedSocial
facebook = RedSocial("Facebook")  # Crea una instancia de RedSocial con nombre "Facebook"

# Agregar usuarios a la red social
facebook.agregar_usuario("Juan")
facebook.agregar_usuario("María")

# Mostrar los usuarios de la red social
facebook.mostrar_usuarios()
