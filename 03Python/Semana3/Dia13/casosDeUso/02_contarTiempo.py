import time


def contar_tiempo(funcion):

    def medir_duracion(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        print("Tiempo (s):", time.time() - inicio)

    return medir_duracion


@contar_tiempo
def crear_diccionario():
    diccionario = {
        "nombre": "Ana",
        "apellido": "Pinto",
    }
    time.sleep(2)
    return diccionario


crear_diccionario()
