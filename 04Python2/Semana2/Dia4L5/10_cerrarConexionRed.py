import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.ejemplo.com", 80))
    print("Conexión establecida.")
    # Realizar operaciones con la conexión
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    if 's' in locals():
        s.close()
        print("Conexión cerrada.")
