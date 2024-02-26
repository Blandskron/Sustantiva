class User:
    def __init__(self, name, age):
        """
        Constructor de la clase User.

        Args:
        - name (str): Nombre del usuario.
        - age (int): Edad del usuario.
        """
        self._name = name  # Establece el nombre del usuario
        self._age = age  # Establece la edad del usuario
        self._friends = []  # Inicializa la lista de amigos del usuario
        self._messages = []  # Inicializa la lista de mensajes del usuario

    def addFriend(self, friend):
        """
        Agrega un amigo a la lista de amigos del usuario.

        Args:
        - friend (User): Usuario amigo que se agrega a la lista de amigos.
        """
        self._friends.append(friend)  # Agrega el amigo a la lista de amigos

    def sendMessage(self, message, friend):
        """
        Envía un mensaje a un amigo y lo guarda en la lista de mensajes del usuario y del amigo.

        Args:
        - message (str): Mensaje a enviar.
        - friend (User): Usuario amigo al que se le envía el mensaje.
        """
        self._messages.append(message)  # Agrega el mensaje a la lista de mensajes del usuario
        friend._messages.append(message)  # Agrega el mensaje a la lista de mensajes del amigo

    def showMessages(self):
        """
        Devuelve la lista de mensajes del usuario.
        """
        return self._messages  # Devuelve la lista de mensajes del usuario

    @property
    def name(self):
        """
        Propiedad para obtener el nombre del usuario.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter para actualizar el nombre del usuario.

        Args:
        - value (str): Nuevo valor para el nombre del usuario.
        """
        self._name = value  # Actualiza el nombre del usuario

    @property
    def age(self):
        """
        Propiedad para obtener la edad del usuario.
        """
        return self._age

    @age.setter
    def age(self, value):
        """
        Setter para actualizar la edad del usuario.

        Args:
        - value (int): Nueva edad del usuario.
        """
        self._age = value  # Actualiza la edad del usuario
