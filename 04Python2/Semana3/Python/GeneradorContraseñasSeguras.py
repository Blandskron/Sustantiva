import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud_usuario = int(input("Ingrese la longitud de la contraseña: "))
print("Contraseña Generada:", generar_contrasena(longitud_usuario))
