# Importa el módulo time para trabajar con el tiempo
import time

# Define el intervalo de tiempo en segundos para el recordatorio (en este caso, cada hora)
intervalo = 60 * 60  # 60 segundos * 60 minutos = 3600 segundos (1 hora)

# Inicializa la cantidad de agua bebida en 0
cantidad_agua = 0

# Bucle infinito que se ejecuta continuamente
while True:
    # Incrementa la cantidad de agua bebida en 250 ml en cada iteración del bucle
    cantidad_agua += 250  # Suponiendo que se beberán 250 ml de agua cada hora
    
    # Imprime un mensaje que indica la cantidad total de agua bebida hasta el momento
    print(f"Has bebido {cantidad_agua} ml de agua hasta ahora.")
    
    # La función sleep() pausa la ejecución del programa durante el intervalo especificado (1 hora)
    # Esto hace que el programa espere antes de continuar con la próxima iteración del bucle
    time.sleep(intervalo)
