# Importamos el módulo time para medir el tiempo.
import time

# Definimos el decorador contar_tiempo.
def contar_tiempo(funcion):
    # Definimos una función interna para medir la duración de la ejecución de la función original.
    def medir_duracion(*args, **kwargs):
        inicio = time.time()  # Tomamos el tiempo de inicio.
        funcion(*args, **kwargs)  # Ejecutamos la función original con sus argumentos.
        print("Tiempo (s):", time.time() - inicio)  # Calculamos y mostramos la duración.

    return medir_duracion  # Retornamos la función interna.

# Definimos una función llamada crear_diccionario que crea un diccionario y simula un proceso con time.sleep().
@contar_tiempo  # Decoramos la función con el decorador contar_tiempo.
def crear_diccionario():
    diccionario = {
        "nombre": "Ana",
        "apellido": "Pinto",
    }
    time.sleep(2)  # Simulamos un proceso que tarda 2 segundos.
    return diccionario

# Llamamos a la función decorada.
crear_diccionario()
