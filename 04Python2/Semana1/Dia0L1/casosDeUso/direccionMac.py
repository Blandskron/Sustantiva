# Importa la función getnode del módulo uuid
from uuid import getnode

# Definición de la función para obtener la dirección MAC
def obtener_direccion_mac():
    # Obtiene la dirección MAC en forma hexadecimal
    mac = hex(getnode())
    # Remueve el prefijo '0x' y convierte a mayúsculas
    mac = mac.replace("0x", "").upper()
    # Asegura que la longitud de la cadena sea de 12 caracteres
    mac = mac.zfill(12)
    # Formatea la dirección MAC con separadores ':' cada dos caracteres
    direccion_mac = ":".join(mac[i: i+2] for i in range(0, 11, 2))
    return direccion_mac

# Llama a la función para obtener la dirección MAC y la imprime
direccion_mac = obtener_direccion_mac()
print(direccion_mac)
