# Importar el módulo de saludos
import saludos

# Definir la función principal del programa
def main():
    # Solicitar al usuario su nombre
    nombre = input("Por favor, introduce tu nombre: ")
    
    # Llamar a la función de saludo del módulo con el nombre proporcionado
    saludos.saludar(nombre)

# Verificar si este script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Si es así, llamar a la función principal
    main()
