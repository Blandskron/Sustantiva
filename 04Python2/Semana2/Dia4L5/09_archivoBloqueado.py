lock = threading.Lock()

try:
    with lock:
        print("Bloqueo adquirido.")
        # Realizar operaciones con el archivo bloqueado
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    if lock.locked():
        lock.release()
        print("Bloqueo liberado.")
