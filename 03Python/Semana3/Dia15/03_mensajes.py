# Definición de la función filter_user_messages() que filtra los mensajes por usuario
def filter_user_messages(messages, user):
    # Filtra los mensajes donde el remitente es el usuario especificado
    filtered_messages = filter(lambda msg: msg['sender'].lower() == user.lower(), messages)
    # Convierte el resultado filtrado a una lista
    return list(filtered_messages)

# Llamada a la función filter_user_messages() con una lista de mensajes y un usuario
response = filter_user_messages([
  {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
  {'sender': 'Bob', 'content': '¡Bien, gracias!'},
  {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
  {'sender': 'Charlie', 'content': 'Hola a todos.'},
  {'sender': 'Alice', 'content': 'Nos vemos luego.'}
], "alice")

# Imprime la lista de mensajes filtrados por el usuario
print(response)
