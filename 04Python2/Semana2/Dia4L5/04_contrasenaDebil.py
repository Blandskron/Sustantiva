class ContrasenaDebilError(Exception):
    def __init__(self, mensaje="La contraseña proporcionada es débil."):
        super().__init__(mensaje)

def verificar_contrasena(contrasena):
    if len(contrasena) < 8:
        raise ContrasenaDebilError("La contraseña debe tener al menos 8 caracteres.")

# Ejemplo de uso
try:
    contrasena = "abc123"
    verificar_contrasena(contrasena)
except ContrasenaDebilError as e:
    print("Error de contraseña:", e)
