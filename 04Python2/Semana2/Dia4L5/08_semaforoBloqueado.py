import threading
import time

semaphore = threading.Semaphore()

try:
    semaphore.acquire()
    print("Recurso adquirido.")
    # Realizar operaciones con el recurso
    time.sleep(2)
except Exception as e:
    print("Ocurrió un error:", e)
finally:
    semaphore.release()
    print("Recurso liberado.")
